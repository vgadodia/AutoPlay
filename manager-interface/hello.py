
"""Simple Hello World example with PyQt5."""

import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

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

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec_())