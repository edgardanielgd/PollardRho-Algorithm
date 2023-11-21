# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainClient.UI'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
from . import ClientResources_rc

class ClientUI_Interface(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 399)
        MainWindow.setStyleSheet(u"background : url(:/images/background.jpg);\n"
"background-color: red;\n"
"background-repeat: no-repeat;\n"
"background-clip:padding-box;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 491, 41))
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(27)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background: transparent;")
        self.label.setTextFormat(Qt.RichText)
        self.lblInbox = QLabel(self.centralwidget)
        self.lblInbox.setObjectName(u"lblInbox")
        self.lblInbox.setGeometry(QRect(390, 180, 331, 21))
        font1 = QFont()
        font1.setFamilies([u"MS PGothic"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.lblInbox.setFont(font1)
        self.lblInbox.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblInbox.setTextFormat(Qt.RichText)
        self.lstInboxMessages = QListWidget(self.centralwidget)
        self.lstInboxMessages.setObjectName(u"lstInboxMessages")
        self.lstInboxMessages.setGeometry(QRect(390, 210, 331, 161))
        self.lstInboxMessages.setStyleSheet(u"background: transparent;\n"
"background-color:white;\n"
"color: black;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 251, 321))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lblSecureMessage_2 = QLabel(self.frame)
        self.lblSecureMessage_2.setObjectName(u"lblSecureMessage_2")
        self.lblSecureMessage_2.setGeometry(QRect(10, 10, 231, 21))
        self.lblSecureMessage_2.setFont(font1)
        self.lblSecureMessage_2.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblSecureMessage_2.setTextFormat(Qt.RichText)
        self.lblSecureMessage = QLabel(self.frame)
        self.lblSecureMessage.setObjectName(u"lblSecureMessage")
        self.lblSecureMessage.setGeometry(QRect(20, 160, 221, 21))
        self.lblSecureMessage.setFont(font1)
        self.lblSecureMessage.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblSecureMessage.setTextFormat(Qt.RichText)
        self.txtTargetHostname = QTextEdit(self.frame)
        self.txtTargetHostname.setObjectName(u"txtTargetHostname")
        self.txtTargetHostname.setGeometry(QRect(50, 40, 171, 31))
        self.txtTargetHostname.setStyleSheet(u"color: white;")
        self.lblSecureMessage_3 = QLabel(self.frame)
        self.lblSecureMessage_3.setObjectName(u"lblSecureMessage_3")
        self.lblSecureMessage_3.setGeometry(QRect(10, 80, 231, 21))
        self.lblSecureMessage_3.setFont(font1)
        self.lblSecureMessage_3.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblSecureMessage_3.setTextFormat(Qt.RichText)
        self.txtTargetPort = QTextEdit(self.frame)
        self.txtTargetPort.setObjectName(u"txtTargetPort")
        self.txtTargetPort.setGeometry(QRect(50, 120, 171, 31))
        self.txtTargetPort.setStyleSheet(u"color: white;")
        self.txtSecureMessage = QPlainTextEdit(self.frame)
        self.txtSecureMessage.setObjectName(u"txtSecureMessage")
        self.txtSecureMessage.setGeometry(QRect(40, 190, 181, 81))
        font2 = QFont()
        font2.setPointSize(16)
        self.txtSecureMessage.setFont(font2)
        self.txtSecureMessage.setStyleSheet(u"background-color:white;\n"
"background:none;\n"
"color: black;")
        self.btnSendMessage = QPushButton(self.frame)
        self.btnSendMessage.setObjectName(u"btnSendMessage")
        self.btnSendMessage.setGeometry(QRect(90, 280, 101, 31))
        self.btnSendMessage.setFont(font2)
        self.btnSendMessage.setStyleSheet(u"color:white;")
        self.txtReceivingPort = QTextEdit(self.centralwidget)
        self.txtReceivingPort.setObjectName(u"txtReceivingPort")
        self.txtReceivingPort.setGeometry(QRect(340, 80, 171, 31))
        self.txtReceivingPort.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.lblSecureMessage_4 = QLabel(self.centralwidget)
        self.lblSecureMessage_4.setObjectName(u"lblSecureMessage_4")
        self.lblSecureMessage_4.setGeometry(QRect(310, 50, 231, 21))
        self.lblSecureMessage_4.setFont(font1)
        self.lblSecureMessage_4.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblSecureMessage_4.setTextFormat(Qt.RichText)
        self.btnConnect = QPushButton(self.centralwidget)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(310, 120, 101, 31))
        self.btnConnect.setFont(font2)
        self.btnConnect.setStyleSheet(u"color:white;\n"
"background-color: black;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: red;")
        self.btnDisconnect = QPushButton(self.centralwidget)
        self.btnDisconnect.setObjectName(u"btnDisconnect")
        self.btnDisconnect.setGeometry(QRect(420, 120, 101, 31))
        self.btnDisconnect.setFont(font2)
        self.btnDisconnect.setStyleSheet(u"color:white;\n"
"background-color: black;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: red;")
        self.lblSecureMessage_5 = QLabel(self.centralwidget)
        self.lblSecureMessage_5.setObjectName(u"lblSecureMessage_5")
        self.lblSecureMessage_5.setGeometry(QRect(570, 50, 231, 21))
        self.lblSecureMessage_5.setFont(font1)
        self.lblSecureMessage_5.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.lblSecureMessage_5.setTextFormat(Qt.RichText)
        self.txtPrivateKey = QTextEdit(self.centralwidget)
        self.txtPrivateKey.setObjectName(u"txtPrivateKey")
        self.txtPrivateKey.setGeometry(QRect(590, 80, 171, 31))
        self.txtPrivateKey.setStyleSheet(u"background-color: black;\n"
"color: white;")
        self.btnGenerateKey = QPushButton(self.centralwidget)
        self.btnGenerateKey.setObjectName(u"btnGenerateKey")
        self.btnGenerateKey.setGeometry(QRect(530, 120, 121, 31))
        self.btnGenerateKey.setFont(font2)
        self.btnGenerateKey.setStyleSheet(u"color:white;\n"
"background-color: black;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: red;")
        self.btnClearCache = QPushButton(self.centralwidget)
        self.btnClearCache.setObjectName(u"btnClearCache")
        self.btnClearCache.setGeometry(QRect(660, 120, 121, 31))
        self.btnClearCache.setFont(font2)
        self.btnClearCache.setStyleSheet(u"color:white;\n"
"background-color: black;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: red;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"A secure application :)", None))
        self.lblInbox.setText(QCoreApplication.translate("MainWindow", u"Your inbox", None))
        self.lblSecureMessage_2.setText(QCoreApplication.translate("MainWindow", u"Target Hostname", None))
        self.lblSecureMessage.setText(QCoreApplication.translate("MainWindow", u"Your secure message:", None))
        self.lblSecureMessage_3.setText(QCoreApplication.translate("MainWindow", u"Target Port", None))
        self.txtSecureMessage.setPlainText("")
        self.btnSendMessage.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.lblSecureMessage_4.setText(QCoreApplication.translate("MainWindow", u"Receiving Port", None))
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btnDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.lblSecureMessage_5.setText(QCoreApplication.translate("MainWindow", u"Private key", None))
        self.btnGenerateKey.setText(QCoreApplication.translate("MainWindow", u"Generate key", None))
        self.btnClearCache.setText(QCoreApplication.translate("MainWindow", u"Clear cache", None))
    # retranslateUi

