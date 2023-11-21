from app.Workers.ProxyWorker import createThread
from app.Algorithms.EllipticCurves import Point, EllipticCurve
from app.Algorithms.PollardRhoBig import pollard_rho
from app.Algorithms.Client import AlgorithmClient
import socket
import re

class RogueConnection:
  def __init__(self, source_hostname, source_id_port, destination_hostname, destination_port):
    self.source_hostname = source_hostname
    self.source_id_port = source_id_port
    self.destination_hostname = destination_hostname
    self.destination_port = destination_port
    self.intercept = False
    self.block_response = False
    self.algorithm = None

    # Origin's keys
    self.private_key = None
    self.public_key = None

  @staticmethod
  def find(list, source_hostname, source_id_port):
    connections = []
    for item in list:
      if item.source_hostname == source_hostname and item.source_id_port == source_id_port:
        connections.append(item)
    return connections

class RogueProxy():
  def __init__(self, curve, port):
    super(RogueProxy, self).__init__()
    self.port = port
    self.curve = curve
    self.connections = []

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind(("", port))
    self.socket.listen(100)

    self.thread = createThread(self.onNewClient)
    self.thread.start()

    print(f"Proxy listenning on port {port}")

  def onNewClient(self):
    while True:
      conn, addr = self.socket.accept()
      print(f"Proxy connected by {addr}")
      worker = createThread(self.processMessage, conn, addr)
      worker.start()
    
  def processMessage(self, conn, addr):
    with conn:
      data = ""
      while True:
          tmp_data = conn.recv(1024)
          if not tmp_data:
              break
          data += tmp_data.decode()
      
      regex = re.compile( r"(.*):(.*):(.*)" )
      match = regex.match(data)

      if match is None:
        return
      
      type = match.group(1)
      peer_port = match.group(2)
      message = match.group(3)

      print(type, peer_port, message)
      
      # Handle data
      connections = RogueConnection.find(self.connections, addr[0], int(peer_port))

      if len(connections) == 0:
        conn.sendall(b"ACK")
        conn.close()
        return

      for connection in connections:
        if connection.intercept:
          print(f"Intercepting Origin {connection.source_hostname}:{connection.source_id_port} -> {connection.destination_hostname}:{connection.destination_port}")

          if type == "key_exchange_response":
            pair = message[-1]
            key = message[:-1]

            try:
                key = int(key)
                pair = int(pair)
            except:
                return

            # It's a compressed key
            compressed = (key, pair)
            key = self.curve.decompressPoint(compressed)

            # Save the origin's public key
            connection.public_key = key

          if type == "message":
            # Get points in message
            separated_points = message.split(",")
            points = []
            c1 = None

            for word in separated_points:
                pair = word[-1]
                msg = word[:-1]

                try:
                  msg = int(msg)
                  pair = int(pair)
                except:
                  return

                # It's a compressed key
                compressed = (msg, pair)
                point = self.curve.decompressPoint(compressed)

                if c1 is None:
                  c1 = point
                else:
                  points.append(point)

            print("==== Intercepted points (Encrypted) ====")
            print("C1",c1)
            for point in points:
              print(point, end=" ")
            print()

            # Get target private key
            target_connections = RogueConnection.find(self.connections, connection.destination_hostname, connection.destination_port)

            if len(target_connections) == 0:
              print("Target not found")
              return
            
            target_connection = target_connections[0]
            
            # Check if we have the private key
            if target_connection.private_key is None:
              print("Private key not found")
            else:
              print("Private key found:", target_connection.private_key)

              # Decrypt
              decrypted = target_connection.algorithm.decrypt(c1, points)

              print("Decrypted")
              msg_data = ""
              for point in decrypted:
                print(point, end=" ")
                if (point.x, point.y) in self.curve.point2Char:
                    msg_data += self.curve.point2Char[(point.x, point.y)]

              print()
              print("Message cleared", msg_data)

        data = f"{type}:{self.port}:{message}"

        # Send the message to the destination
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((connection.destination_hostname, connection.destination_port))
        client_socket.sendall(data.encode())
        
      conn.sendall(b"ACK")

  def sendMessage(self, id, message):
    connection = self.connections[id]
    print(f"Sending message to {connection.source_hostname}:{connection.source_id_port} -> {connection.destination_hostname}:{connection.destination_port}")

    # Get target's public key
    target_connection = RogueConnection.find(self.connections, connection.destination_hostname, connection.destination_port)

    if len(target_connection) == 0:
      print("Target not found")
      return
    
    target_connection = target_connection[0]

    # Check if we have the public key
    if target_connection.public_key is None:
      print("Public key not found")
      return
    
    algorithm = AlgorithmClient(self.curve, connection.private_key, False)
        
    # Encrypt message
    points = []
    for character in message:
        if character in self.curve.char2Points:
            point = self.curve.char2Points[character]
            points.append(point)

    # Encrypt message
    c1, c2 = algorithm.encrypt(target_connection.public_key, points)
    
    x, pair = self.curve.compressPoint(c1)
    message = f"message:{self.port}:{x}{int(pair)},"

    for point_id in range(len(c2)):
        point = c2[point_id]
        x, pair = self.curve.compressPoint(point)
        
        message += f"{point.x}{int(pair)}"

        if point_id < len(c2) - 1:
            message += ","

    # Send the message to the destination
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((connection.destination_hostname, connection.destination_port))
    client_socket.sendall(message.encode())
    
  def findPrivate(self, id):
    connection = self.connections[id]
    print(f"Finding private key for {connection.source_hostname}:{connection.source_id_port} -> {connection.destination_hostname}:{connection.destination_port}")

    # Find private key
    private_key = pollard_rho(self.curve, connection.public_key)
    print(f"Private key found: {private_key}")

    # Save the origin's private key
    connection.private_key = private_key
    connection.algorithm = AlgorithmClient(self.curve, private_key)

  def remove_connection(self, id):
    self.connections.pop(id)

  def add_connection(self, source_hostname, source_id_port, destination_hostname, destination_port):
    connection = RogueConnection(source_hostname, source_id_port, destination_hostname, destination_port)
    self.connections.append(connection)

  def start_intercepting(self, id):
    self.connections[id].intercept = True

  def stop_intercepting(self, id):
    self.connections[id].intercept = False

  def block_response(self, id):
    self.connections[id].block_response = True

  def unblock_response(self, id):
    self.connections[id].block_response = False

  def __str__(self):
    info = "Server listenning on port {}\n".format(self.port)
    for i, connection in enumerate(self.connections):
      info += f"{i} - {connection.source_hostname}:{connection.source_id_port} -> {connection.destination_hostname}:{connection.destination_port}"
      info += " (Intercepting)" if connection.intercept else ""
      info += " (Blocking response)" if connection.block_response else ""
      info += f" Private Key: {connection.private_key}" if connection.private_key is not None else ""
      info += f" Public Key: {connection.public_key}" if connection.public_key is not None else ""
      info += "\n"

    return info