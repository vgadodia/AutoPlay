import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QPalette, QColor, QPixmap
from PyQt5.QtCore import pyqtSlot
from pymongo import MongoClient
from pymongo.collection import ObjectId
import bcrypt
import requests
import json


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'AutoPlay'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.loginText = QLabel('<h1>Welcome to AutoPlay</h1>', self)
        self.loginText.move(275, 180)
        self.loginText.setFixedWidth(300)

        self.button = QPushButton("Login", self)
        self.button.move(315, 260)
        self.button.setFixedSize(180, 35)

        self.button = QPushButton("Register", self)
        self.button.move(315, 315)
        self.button.setFixedSize(180, 35)

        # Trying to display image
        # self.label = QLabel(self)
        # self.pixmap = QPixmap('image.png')
        # self.label.setPixmap(self.pixmap)
        # self.setCentralWidget(self.label)

        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        print("Hello")
        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        # self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(53, 53, 53))
    palette.setColor(QPalette.AlternateBase, QColor(30, 30, 30))
    palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
    app.setPalette(palette)
    ex = App()
    sys.exit(app.exec_())