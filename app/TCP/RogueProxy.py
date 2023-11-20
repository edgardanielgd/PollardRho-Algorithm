from app.Workers.ProxyWorker import createThread
from app.Algorithms.EllipticCurves import Point, EllipticCurve
from app.Algorithms.PollardRhoBig import pollard_rho
import socket
import re

class RogueConnection:
  def __init__(self, source_hostname, destination_hostname, destination_port):
    self.source_hostname = source_hostname
    self.destination_hostname = destination_hostname
    self.destination_port = destination_port
    self.intercept = False
    self.block_response = False

    # Origin's keys
    self.private_key = None
    self.public_key = None

  @staticmethod
  def find(list, source_hostname):
    for item in list:
      if item.source_hostname == source_hostname:
        return item
    return None

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
      
      # Handle data
      connection = RogueConnection.find(self.connections, addr[0])

      if connection is None:
        conn.sendall(b"ACK")
        conn.close()
        return

      if connection.intercept:
        print(f"Intercepting Origin {connection.source_hostname} -> {connection.destination_hostname}:{connection.destination_port}")
        
        # Destructure the message
        regex = re.compile( r"(.*):(.*):(.*)" )
        match = regex.match(data)

        print(data)

        if match is None:
            return
        
        type = match.group(1)
        peer_port = match.group(2)
        message = match.group(3)

        if type == "key_exchange_response":
          pair = message[-1]
          key = message[:-1]

          try:
              key = int(key)
              pair = int(pair)
          except:
              return

          # It's a compressed key
          data = (key, pair)
          key = self.curve.decompressPoint(data)

          # Save the origin's public key
          connection.public_key = key

          # Process key with Pollard Rho
          print("Pollard Rho")
          connection.private_key = pollard_rho(self.curve, key)

          print(f"Key for {addr} Obtained!, {key}")


        print(type, peer_port, message)

      # Send the message to the destination
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect((connection.destination_hostname, connection.destination_port))
      client_socket.sendall(data.encode())

      # Receive the response
      # response = ""
      # while True:
      #     tmp_data = client_socket.recv(1024)
      #     print(tmp_data.decode())
      #     if not tmp_data:
      #         break
      #     response += tmp_data.decode()
      
      # print("Sent")

      # if connection.intercept:
      #   print(f"Intercepting Destination {connection.destination_hostname}:{connection.destination_port} -> {connection.source_hostname}")
      #   print(response)

      # # Send the response to the source
      # if connection.block_response:
      #   print("Blocking response")
      #   response = ""
        
      conn.sendall(b"ACK")

  def remove_connection(self, id):
    self.connections.pop(id)

  def add_connection(self, source_hostname, destination_hostname, destination_port):
    connection = RogueConnection(source_hostname, destination_hostname, destination_port)
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
      info += f"{i} - {connection.source_hostname} -> {connection.destination_hostname}:{connection.destination_port}\n"

    return info