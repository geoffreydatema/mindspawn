import sys
from utils.utils import *
import utils.accountutils as accountutils
import PyQt5.QtWidgets as qt
from ui.MainWindow import *

def main():

    # account = accountutils.initAccountFile(username="oystertheory")

    # print(account)

    app = qt.QApplication(sys.argv + ["-platform", "windows:darkmode=1"])
    window = MainWindow()
    app.exec_()

if __name__ == '__main__':
    main()