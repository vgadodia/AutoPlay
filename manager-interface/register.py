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

def register_manager(email, password, spotify):
    if db.managers.find_one({"email":email}) == None:
        hashp = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        k = {"email":email, "password":hashp, "spotify":spotify, "songs":[]}
        db.managers.insert_one(k)
        return {"status":"success"}
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

        self.loginText = QLabel('<h1>Register</h1>', self)
        self.loginText.move(355, 80)
        self.loginText.setFixedWidth(200)

        
        self.errorText = QLabel('', self)
        self.errorText.setFixedWidth(400)
        self.errorText.setStyleSheet("color: #FFFF12") 
        self.errorText.move(300, 385)

        self.button = QPushButton("Sign up", self)
        self.button.move(325, 300)
        self.button.setFixedWidth(150)

        self.backbutton = QPushButton("Back", self)
        self.backbutton.move(325, 345)
        self.backbutton.setFixedWidth(150)

        self.email = QLineEdit(self)
        self.userid = QLineEdit(self)
        self.password = QLineEdit(self)
        self.confirmpassword = QLineEdit(self)


        self.userid.setPlaceholderText("  Spotify ID")
        self.password.setPlaceholderText("  Password")
        self.email.setPlaceholderText("  Email")
        self.confirmpassword.setPlaceholderText("  Confirm Password")

        self.password.setEchoMode(QLineEdit.Password)
        self.confirmpassword.setEchoMode(QLineEdit.Password)
        self.userid.setFixedWidth(200)
        self.email.setFixedWidth(200)
        self.confirmpassword.setFixedWidth(200)
        self.password.setFixedWidth(200)

        self.email.move(300, 130)
        self.userid.move(300, 170)
        self.password.move(300, 210)
        self.confirmpassword.move(300, 250)

        self.button.clicked.connect(self.on_click)
        self.backbutton.clicked.connect(self.backbutton_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        email = self.email.text().strip()
        pwd = self.password.text().strip()
        sid = self.userid.text().strip()
        cpwd = self.confirmpassword.text().strip()

        if len(email) > 0 and len(pwd) > 0 and len(sid) > 0 and len(cpwd) > 0 and pwd == cpwd:
            k = register_manager(email, pwd, sid)
            if k["status"] == "success":
                self.errorText.setText("Registered successfully")
            else:
                self.errorText.setText("An account with This email already exists.")
        else:
            self.errorText.setText("Invalid Credentials. Please try again.")
    
    @pyqtSlot()
    def backbutton_click(self):
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