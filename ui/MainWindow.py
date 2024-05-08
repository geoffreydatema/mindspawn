import PyQt5.QtWidgets as qt

class MainWindow(qt.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mindspawn 0.0.1")
        self.setLayout(qt.QVBoxLayout())
        self.setup()
        self.show()

    def setup(self):
        container = qt.QWidget()
        container.setLayout(qt.QGridLayout())
        message = qt.QLabel("hello world")
        container.layout().addWidget(message)
        self.layout().addWidget(container)