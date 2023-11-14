import socket
from threading import Thread

class Proxy2Server(Thread):
  def __init__(self, host, port):
    super(Proxy2Server, self).__init__()
    self.client = None  #interface client socket
    self.port = port
    self.host=host
    self.server = socket.socket(socket.AF_INET,     
                                socket.SOCK_STREAM)
    self.server.connect((host, port))
  
  def run(self):
    while True:
      data= self.server.recv(4096)
      if data:
        self.client.sendall(data)
        

class Client2Proxy(Thread):
  def __init__(self, host, port):
    super(Client2Proxy, self).__init__()
    self.server = None  #interface server socket
    self.port = port
    self.host=host
    sock = socket.socket(socket.AF_INET,     
                                socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    #Waiting for a connection
    self.client, addr = sock.accept()

  def run(self):
    while True:
      data= self.client.recv(4096)
      if data:
        self.server.sendall(data)

class Proxy(Thread):
  def __init__(self, from_host, to_host, port):
    super(Proxy, self).__init__()
    self.from_host = from_host
    self.to_host = to_host
    self.port = port
    

  def run(self):
    while True:
      print ("[proxy({})] setting up".format(self.port))
      self.c2p = Client2Proxy(self.from_host, self.port)
      self.p2s = Proxy2Server(self.to_host, self.port)
      print ("[proxy({})] connection established".format(self.port))
      self.c2p.server = self.p2s.server
      self.p2s.client = self..server
      
      self.c2p.start()
      self.p2s.start()




        
        
      