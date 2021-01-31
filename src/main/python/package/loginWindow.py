from PySide2.QtWidgets import *
from PySide2.QtCore import *

from package.api.sendsms import *


class LoginWindow(object):
    def __init__(self):
        super().__init__()

        self.sendCode = sendSms()
        # self.sendCode = 2
        self.confirm_user = True

    def setup_ui(self, login):
        self.create_widgets(login)
        self.modify_widgets()
        self.create_layout(login)
        self.add_widgets_to_layout(login)
        self.retranslate_ui(login)
        self.setup_connections(login)
        QMetaObject.connectSlotsByName(login)

    def create_widgets(self, login):
        self.label = QLabel(login)
        self.label.setObjectName("consigne")

        self.entry = QLineEdit(login)
        self.entry.setObjectName("code_sms")

        self.button = QDialogButtonBox(login)
        self.button.setOrientation(Qt.Horizontal)
        self.button.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.button.setObjectName("buttons")

    def modify_widgets(self):
        pass

    def create_layout(self, login):
        self.layout = QVBoxLayout(login)
        self.layout.setObjectName("layout")

    def add_widgets_to_layout(self, login):
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)
        # self.layout

    def retranslate_ui(self, login):
        _translate = QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Connexion"))
        self.label.setText(_translate("login", "Veuillez renseigner le code reçu par SMS"))

    def setup_connections(self, login):
        # self.button.clicked.connect(self.codeVerification)
        self.button.rejected.connect(login.reject)
        self.button.accepted.connect(lambda: self.codeVerification(login))

    # END UI

    def codeVerification(self, login):
        user_code = self.user_code_verify()

        if user_code == int(self.sendCode):
            print("code Exact")
            self.confirm_user = True
            return login.accept()
        else:
            print("Code Incorrect")

    def exit_app(self):
        self.close()

    def user_code_verify(self):
        code_int = 0

        code_str = self.entry.text()
        try:
            code_int = int(code_str)
            return code_int
        except ValueError as e:
            print("Erreur! Le code rentré n'est pas valide. Réessayer!")
            return e


