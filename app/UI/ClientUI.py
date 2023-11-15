from app.UI.resources.python.ClientUI_Interface import ClientUI_Interface
from PySide6.QtWidgets import QMainWindow
from app.Algorithms.Client import AlgorithmClient
from app.Algorithms.EllipticCurves import EllipticCurve

import PySide6.QtWidgets as QtWidgets

class ClientUI(QMainWindow, ClientUI_Interface):
    def __init__(self, curve : EllipticCurve, key : int):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)

        # Initialize algorithm
        self.algorithm = AlgorithmClient(curve, key)

    def sendMessage(self):
        points = []

        # Parse input to points
        for character in self.plainTextEdit.toPlainText():
            point = self.algorithm.curve.char2Points[character]
            points.append(point)

        # Encrypt message
        c1, c2 = self.algorithm.encrypt(self.algorithm.getPubKey(), points)

        return c1,c2