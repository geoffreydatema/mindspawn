import sys
from utils.utils import *
import utils.accountutils as accountutils
import PyQt5.QtWidgets as qt
from ui.MainWindow import *
from core.Account import Account

def main():
  
    account = Account()

    app = qt.QApplication(sys.argv + ["-platform", "windows:darkmode=1"])
    window = MainWindow(account)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()