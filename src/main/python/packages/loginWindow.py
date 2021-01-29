from PySide2.QtWidgets import *
from PySide2.QtCore import *

from packages.api.sendsms import *

class LoginWindow(QWidget):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("Connexion")
        self.resize(200, 150)

        # self.sendCode = sendSms()
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layout()
        self.setup_connections()

    def create_widgets(self):
        self.label = QLabel("Veuillez renseigner le code reçu par sms")
        self.entry = QLineEdit()
        self.button = QPushButton("Valider")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())
        self.entry.width = 100

    def create_layout(self):
        self.layout = QVBoxLayout()

    def add_widgets_to_layout(self):
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def setup_connections(self):
        self.button.clicked.connect(self.codeVerification)

    # END UI
    def exit_app(self):
        self.close()

    def codeVerification(self):
        print("verification du code")
