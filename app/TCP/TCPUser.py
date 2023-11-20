import socket
from threading import Thread
from app.Workers.DefaultWorker import createThread
from PySide6.QtCore import QThreadPool

class TCPUser():
    def __init__(self, callback):

        self.threadpool = QThreadPool.globalInstance()
        self.self_port = 8000
        self.socket = None

        self.callback = callback
        
    def connect(self, port=None):
        if self.socket is not None:
            return
        
        if port is not None:
            self.self_port = port
        
        # Listen for messages in self_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('', self.self_port))
        self.socket.listen()

        # Initialize worker
        self.thread = createThread(self.onNewClient)
        self.thread.start()

        print("Server listenning on port {}".format(self.self_port))

    def disconnect(self):
        if self.socket is None:
            return
        
        self.socket.close()
        self.socket = None

        self.thread.quit()

        print("Server disconnected")
        
    def send(self, host, port, message : str):

        if self.socket is None:
            return
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        client_socket.close()

    def receive(self, conn, addr):
        with conn:
            data = ""
            while True:
                tmp_data = conn.recv(1024)
                if not tmp_data:
                    break
                data += tmp_data.decode()

            self.callback(data, addr)
            
            # Send an ACK message and Close connection
            conn.sendall(b"ACK")
            conn.close()

    def onNewClient(self):
        while True:
            conn, addr = self.socket.accept()
            print(f"Connected by {addr}")
            worker = createThread(self.receive, conn, addr)
            worker.start()