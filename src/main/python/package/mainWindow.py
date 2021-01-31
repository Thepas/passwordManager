from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from package.api.password import *
from package.mainTab import MainTab
from package.historyTab import HistoryTab

class MainWindow(QMainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("Password Manager")
        print("draaa")
        self.setup_ui()

    def setup_ui(self):
        self.create_menu()
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("Menu")
        exitAction = QAction("Exit", self)
        exitAction.setShortcut(QtGui.QKeySequence("escape"))
        exitAction.triggered.connect(self.exit_app)
        fileMenu.addAction(exitAction)

    def create_widgets(self):
        self.tabs_widget = QTabWidget()
        self.tab1 = MainTab(self)
        self.tab2 = HistoryTab(self)

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layout(self):
        pass

    def add_widgets_to_layout(self):
        self.setCentralWidget(self.tabs_widget)
        self.tabs_widget.addTab(self.tab1, "Générateur de mot de passe")
        self.tabs_widget.addTab(self.tab2, "identifiants et mots de passe")

    def setup_connections(self):
        pass

    # END UI
    def exit_app(self):
        self.close()

    def resetValue(self):
        pass
