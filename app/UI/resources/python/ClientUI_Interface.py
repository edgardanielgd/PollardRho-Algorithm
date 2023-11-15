# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainClient.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
from . import ClientResources_rc

class ClientUI_Interface(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(597, 276)
        MainWindow.setStyleSheet(u"background-image : url(:/images/pngtree-abstract-technology-background-technical-electric-image_443494.jpg) 0 0 0 0 stretch stretch;\n"
"background-color: black;\n"
"background-repeat: repeat;\n"
"background-clip:padding-box;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 451, 41))
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(27)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background: transparent;")
        self.label.setTextFormat(Qt.RichText)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(40, 100, 261, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"background-color:white;\n"
"background:none;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 261, 21))
        font2 = QFont()
        font2.setFamilies([u"MS PGothic"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.label_2.setTextFormat(Qt.RichText)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 200, 101, 31))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color:white;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 60, 221, 21))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"background:transparent;\n"
"background-color: black;")
        self.label_3.setTextFormat(Qt.RichText)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(340, 100, 231, 151))
        self.listWidget.setStyleSheet(u"background: transparent;\n"
"background-color:white;")
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
        self.plainTextEdit.setPlainText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Your secure message:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Your inbox", None))
    # retranslateUi

