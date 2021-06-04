from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import *
import pandas as pd

from package.api.TableModel import TableModel

class HistoryTab(QtWidgets.QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ctx = mainWindow.ctx
        self.csv_file = self.ctx.get_resource("save/identifiants.csv")
        self.id_df = pd.read_csv(self.csv_file,
                                 dtype={'url': str,
                                        'username': str,
                                        'password': str,
                                        'timeCreated': str,
                                        'timePasswordChanged': str})

        # conversion timestamp to datetime
        self.id_df['timeCreated'] = pd.to_datetime(self.id_df['timeCreated'], unit='ms')
        self.id_df['timePasswordChanged'] = pd.to_datetime(self.id_df['timePasswordChanged'],
                           unit='ms')
        # set model
        self.model = TableModel(self.id_df)

        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widgets(self):
        self.table_view = QtWidgets.QTableView()
        self.setObjectName("tableView")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layout(self):
        self.mainlayout = QtWidgets.QVBoxLayout()

    def add_widgets_to_layout(self):
        self.mainlayout.addWidget(self.table_view)

    def setup_connections(self):
        self.setLayout(self.mainlayout)
        self.table_view.setModel(self.model)

    # END UI
    def exit_app(self):
        self.close()

