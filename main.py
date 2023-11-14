from UI.ClientUI import ClientUI
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

# Construct a QApplication
app = QApplication(sys.argv)
    
# Create a main chat window
mainChat = ClientUI()

mainChat.show()

# Run the event loop
sys.exit(app.exec())