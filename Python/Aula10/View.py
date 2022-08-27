import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.field = QLineEdit(self)
        self.field.move(210, 40)
        self.field.resize(150, 25)

        self.label = QLabel(self)
        self.label.setText("I'm a Label")
        self.label.setStyleSheet("QLabel {font:bold; size: 20px; color: #1CD475}")
        self.label.move(50, 100)
        self.label.resize(230, 40)

        self.button = QPushButton("Click Me", self)
        self.button2 = QPushButton("Crique Me", self)
        self.buttons()

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(200, 100, 700, 600)
        self.setWindowTitle("Primeira Janela")
        self.show()

    def buttons(self):
        self.button.move(430, 100)
        self.button.resize(130, 50)
        self.button.setStyleSheet("QPushButton {background-color: #836FFF}")
        self.button.clicked.connect(self.clicked)

        self.button2.move(230, 100)
        self.button2.resize(130, 50)
        self.button2.setStyleSheet("QPushButton {background-color: #836FFF}")
        self.button2.clicked.connect(self.cricked)

    def clicked(self):
        valor = self.field.text()
        self.label.setText("Valor do campo é: " + valor)
        self.label.setStyleSheet("QLabel {font:bold; size: 20px; color: #0F01B7}")
        self.button.setText("Clicou")

    def cricked(self):
        self.button2.setText("Cricou")

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.field = QLineEdit(self)
        self.field.move(210, 40)
        self.field.resize(150, 25)

        self.label = QLabel(self)
        self.label.setText("I'm a Label")
        self.label.setStyleSheet("QLabel {font:bold; size: 20px; color: #1CD475}")
        self.label.move(50, 100)
        self.label.resize(230, 40)

        self.button = QPushButton("Click Me", self)
        self.button2 = QPushButton("Crique Me", self)
        self.buttons()

        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(800, 100, 700, 600)
        self.setWindowTitle("Segunda Janela")
        self.show()

    def buttons(self):
        self.button.move(430, 100)
        self.button.resize(130, 50)
        self.button.setStyleSheet('QPushButton {background-color: #CC33CC}')
        self.button.clicked.connect(self.clicked)

        self.button2.move(230, 100)
        self.button2.resize(130, 50)
        self.button2.setStyleSheet("QPushButton {background-color:#00BFFF;font-size:20px;font:bold}")
        self.button2.clicked.connect(self.cricked)

    def clicked(self):
        valor = self.field.text()
        self.label.setText("Valor do campo é: " + valor)
        self.label.setStyleSheet("QLabel {font:bold; size: 20px; color: #0F01B7")
        self.button.setText("Cricou")

    def cricked(self):
        self.button2.setText("Cricou")
        print("Oia o crick")


app = QApplication(sys.argv)
w = Window()
y = Window2()
app.exec_()


