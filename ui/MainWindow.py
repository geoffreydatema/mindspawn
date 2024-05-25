import PyQt5.QtWidgets as qt
from data.gamevars import gamevars

class MainWindow(qt.QWidget):
    def __init__(self, account):
        super().__init__()
        self.setWindowTitle(f"Mindspawn {gamevars["version"]}")
        self.setFixedSize(1280, 720)
        self.setLayout(qt.QVBoxLayout())
        self.setup()
        self.setStyles()

        self.show()

    def setup(self):
        self.container = qt.QWidget()
        self.container.setLayout(qt.QGridLayout())

        message = qt.QLabel("hello world")
        
        self.container.layout().addWidget(message)

        self.layout().addWidget(self.container)

    def setStyles(self):
        # top level defaults
        self.setStyleSheet("background-color: black; color: white")
