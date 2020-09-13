import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import pyqtSlot
from pymongo import MongoClient
from pymongo.collection import ObjectId
import bcrypt
import requests
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient("mongodb+srv://user:pwd@cluster0.x4ft0.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.get_database("data")


def login_manager(email, password):
    k = db.managers.find_one({"email":email})

    if k != None:
        x = bcrypt.hashpw(password.encode('utf-8'), k["password"])
        
        
        if x == k["password"]:
            return {"status":"success"}
        else:
            return {"status":"failed"}

    else:
        return {"status":"failed"}

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

        self.loginText = QLabel('<h1>Login</h1>', self)
        self.loginText.move(365, 100)

        
        self.errorText = QLabel('', self)
        self.errorText.setFixedWidth(400)
        self.errorText.setStyleSheet("color: red") 
        self.errorText.move(300, 350)

        self.button = QPushButton("Login", self)
        self.button.move(325, 265)
        self.button.setFixedWidth(150)

        self.backbutton = QPushButton("Back", self)
        self.backbutton.move(325, 310)
        self.backbutton.setFixedWidth(150)

        self.userid = QLineEdit(self)
        self.password = QLineEdit(self)
        self.userid.setPlaceholderText("  Email")
        self.password.setPlaceholderText("  Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.userid.setFixedWidth(200)
        self.password.setFixedWidth(200)
        self.userid.move(300, 175)
        self.password.move(300, 215)
    

        self.button.clicked.connect(self.on_click)
        self.backbutton.clicked.connect(self.back_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        email = self.userid.text().strip()
        password = self.password.text().strip()
        
        if len(email) > 0 and len(password) > 0:
            k = login_manager(email, password)
            if k["status"] == "success":
                self.errorText.setText("Login Successful.")
            else:
                self.errorText.setText("Incorrect email or password.")
        else:
            self.errorText.setText("Invalid credentials. Please retry.")
        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        # self.textbox.setText("")
    @pyqtSlot()
    def back_click(self):
        print("Back button clicked")

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