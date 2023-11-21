from app.UI.resources.python.ClientUI_Interface import ClientUI_Interface
from PySide6.QtWidgets import QMainWindow
from app.Algorithms.Client import AlgorithmClient
from app.Algorithms.EllipticCurves import EllipticCurve

from PySide6.QtCore import QThreadPool
import PySide6.QtWidgets as QtWidgets
from app.TCP.TCPUser import TCPUser

from app.UI.Utils import displayInformationMsg, displayErrorMsg

import re

class ClientUI(QMainWindow, ClientUI_Interface):
    def __init__(self, curve : EllipticCurve ):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # Initialize algorithm
        self.algorithm = None
        self.curve = curve
        self.port = 0

        self.btnSendMessage.clicked.connect(self.sendTCPMessage)
        self.btnGenerateKey.clicked.connect(self.generatePublicKey)

        self.TCPUser = TCPUser(self.receiveMessage)

        self.btnConnect.clicked.connect(self.connect)
        self.btnDisconnect.clicked.connect(self.disconnect)

        self.btnClearCache.clicked.connect(lambda: self.peersKeys.clear())

        # Cache peers public keys
        self.peersKeys = {}

    def connect(self):
        port = self.txtReceivingPort.toPlainText()

        try:
            port = int(port)
        except:
            displayErrorMsg("Error", "Invalid port")
            return 
        
        self.port = port
        self.TCPUser.connect(port)

        self.btnConnect.setEnabled(False)

        displayInformationMsg("Success", "Connected successfully")

        self.lstInboxMessages.addItem(f"[INFO] Listening on port {port}")
    
    def disconnect(self):
        self.TCPUser.disconnect()

        self.btnConnect.setEnabled(True)
        displayInformationMsg("Success", "Disconnected successfully")

        self.lstInboxMessages.addItem(f"[INFO] Disconnected")
    
    def receiveMessage(self, message, address):
        """
        Message structure is:
        <type> : <peer port> : <message>

        Points in message are separated by a comma, being the first the c1 point
        """
        print(message)
        if self.TCPUser.socket is None or self.algorithm is None:
            displayErrorMsg("Error", "Not connected")
            return
        
        regex = re.compile( r"(.*):(.*):(.*)" )
        match = regex.match(message)

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
            self.peersKeys[address[0]] = key

            print(f"Key for {address} received, {key}")

            self.lstInboxMessages.addItem(f"[INFO] Key for {address[0]}:{peer_port} received, {key}")
            return
        
        if type == "key_exchange_request":
            # Send compressed key
            key = self.algorithm.getPubKey()
            compressed = self.curve.compressPoint(key)
            self.TCPUser.send(
                address[0], 
                int(peer_port), 
                f"key_exchange_response:{self.port}:{compressed[0]}{int(compressed[1])}"
            )

            print(f"Key for {address} sent, {key}")
            
            self.lstInboxMessages.addItem(f"[INFO] Key for {address[0]}:{peer_port} sent, {key}")
            return

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
                data = (msg, pair)
                point = self.curve.decompressPoint(data)

                if c1 is None:
                    c1 = point
                    continue 
                    
                points.append(point)

            # Decrypt message
            m = self.algorithm.decrypt(c1, points)

            # Parse points to string
            message = ""
            for point in m:
                if (point.x, point.y) in self.algorithm.curve.point2Char:
                    message += self.algorithm.curve.point2Char[(point.x, point.y)]
                
            # Append messsage to text box
            self.lstInboxMessages.addItem(f"[MESSAGE] Address [{address[0]}:{peer_port}] : {message}")

    def generatePublicKey(self):
        key = self.txtPrivateKey.toPlainText()
        try:
            key = int(key)
        except:
            displayErrorMsg("Error", "Invalid private key")
            return
        
        self.algorithm = AlgorithmClient(self.curve, key)
        displayInformationMsg("Success", "Public key generated")

        print("Public key",self.algorithm.getPubKey())

        self.lstInboxMessages.addItem(f"[INFO] Public key generated, {self.algorithm.getPubKey()}")

    def sendTCPMessage(self):

        if self.TCPUser.socket is None or self.algorithm is None:
            displayErrorMsg("Error", "Not connected")
            return

        hostname = self.txtTargetHostname.toPlainText()
        port = self.txtTargetPort.toPlainText()

        try:
            port = int(port)
        except:
            displayErrorMsg("Error", "Invalid port")
            return
        
        # Check if peer's key is cached, otherwise discard message and request key
        key = None
        if hostname in self.peersKeys:
            key = self.peersKeys[hostname]
        else:
            self.TCPUser.send(
                hostname, 
                port, 
                f"key_exchange_request:{self.port}:"
            )
            displayErrorMsg("Error", "Peer's key not cached, request sent")
            return
        
        # Encrypt message
        points = []
        for character in self.txtSecureMessage.toPlainText():
            if character in self.algorithm.curve.char2Points:
                point = self.algorithm.curve.char2Points[character]
                points.append(point)

        # Encrypt message
        c1, c2 = self.algorithm.encrypt(key, points)
        
        x, pair = self.curve.compressPoint(c1)
        message = f"message:{self.port}:{x}{int(pair)},"

        for point_id in range(len(c2)):
            point = c2[point_id]
            x, pair = self.curve.compressPoint(point)
            
            message += f"{point.x}{int(pair)}"

            if point_id < len(c2) - 1:
                message += ","

        print("Encrypted", message)
        self.TCPUser.send(hostname, port, message)

    def closeEvent(self, event):
        self.TCPUser.disconnect()
        event.accept()