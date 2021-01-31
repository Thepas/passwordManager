from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import *


class HistoryTab(QtWidgets.QWidget):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widgets(self):
        pass

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layout(self):
        pass

    def add_widgets_to_layout(self):
        pass

    def setup_connections(self):
        pass

    # END UI
    def exit_app(self):
        self.close()

