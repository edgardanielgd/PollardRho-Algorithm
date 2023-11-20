from app.UI.ClientUI import ClientUI
from app.Algorithms.EllipticCurves import EllipticCurve, Point
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

# Construct a QApplication
app = QApplication(sys.argv)

curve = EllipticCurve(416,569,659)
g = Point(23,213,curve)
curve.setGenerator(g)

# Create a main chat window
mainChat = ClientUI(curve)

mainChat.show()

# Run the event loop
sys.exit(app.exec())