from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow, QDialog
from PySide2 import QtCore

from package.loginWindow import LoginWindow
from package.mainWindow import MainWindow

import sys


if __name__ == '__main__':
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    # login = QDialog()
    # login.ui = LoginWindow()
    # login.ui.setup_ui(login)
    # login.setWindowModality(QtCore.Qt.ApplicationModal)
    #
    # login.exec_()

    # if(login.ui.confirm_user):
    window = MainWindow(appctxt)
    window.resize(688, 422)
    window.show()


    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
