from PySide6.QtWidgets import QMessageBox

def displayInformationMsg(title, message):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setStyleSheet("QLabel{color:black;}")
    msg.exec()

def displayErrorMsg(title, message):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setStyleSheet("QLabel{color:black;}")
    msg.exec()