from .resources.python.ClientUI_Interface import ClientUI_Interface
from multiprocessing import Process
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QImage, QPixmap
from PySide6 import QtCore

import PySide6.QtWidgets as QtWidgets

class ClientUI(QMainWindow, ClientUI_Interface):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendMessage)

    def sendMessage(self):
        pass