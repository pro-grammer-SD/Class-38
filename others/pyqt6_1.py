# This is coz i hate tkinter

import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.count = 0
        def wee():
            self.count+=1
            print("Hi!", self.count)
        self.button.clicked.connect(wee)
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
