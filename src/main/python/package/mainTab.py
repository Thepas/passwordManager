from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import pyperclip

from package.api.password import *

class MainTab(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ctx = mainWindow.ctx
        self.mainWindow = mainWindow
        # self.setFixedSize(640, 422)
        self.setup_ui()
        # print(mainWindow.width())
        # print(mainWindow.height())

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.createSave_Box()
        # self.saveGroupBox.hide()
        self.add_widgets_to_layout()

        self.setup_connections()

    def create_widgets(self):
        self.tab_img = QLabel()
        self.newPass_label = QLabel("Voici ton nouveau mot de passe:")
        self.pass_box = QLineEdit()
        self.generate_btn = QPushButton("Générer le mot de passe")
        self.copy_btn = QPushButton("Copier le mot de passe")

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        pixmap = QtGui.QPixmap(self.ctx.get_resource("img/password_Icon.png"))
        pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio)
        self.tab_img.setPixmap(pixmap)


    def create_layout(self):
        self.mainTab_layout = QGridLayout()

    def add_widgets_to_layout(self):
        self.mainTab_layout.addWidget(self.tab_img, 0, 0, alignment=Qt.AlignCenter)
        self.mainTab_layout.addWidget(self.newPass_label, 1, 0, alignment=Qt.AlignCenter)
        self.mainTab_layout.addWidget(self.pass_box, 2, 0, alignment=Qt.AlignCenter)
        self.mainTab_layout.addWidget(self.generate_btn, 3,0, alignment=Qt.AlignCenter)
        self.mainTab_layout.addWidget(self.copy_btn, 3,0, alignment=Qt.AlignRight)

    def setup_connections(self):
        self.setLayout(self.mainTab_layout)
        self.generate_btn.clicked.connect(self.getPassword)
        self.saveButton.clicked.connect(self.savePassword)
        self.copy_btn.clicked.connect(self.copyPassword)
    # END UI
    def copyPassword(self):
        pyperclip.copy(self.pass_box.text())

    def createSave_Box(self):
        self.saveGroupBox = QGroupBox("Sauvegarde du mot de passe")
        saveGroupBox_layout = QFormLayout()

        label = QLabel("Site web: ")
        self.entry = QLineEdit()

        label_id = QLabel("identifiant: ")
        self.entry_id = QLineEdit()

        self.saveButton = QPushButton("Sauvegarder")

        saveGroupBox_layout.setWidget(0, QFormLayout.LabelRole, label)
        saveGroupBox_layout.setWidget(0, QFormLayout.FieldRole, self.entry)
        saveGroupBox_layout.setWidget(1, QFormLayout.LabelRole, label_id)
        saveGroupBox_layout.setWidget(1, QFormLayout.FieldRole, self.entry_id)
        saveGroupBox_layout.addWidget(self.saveButton)

        self.saveGroupBox.setLayout(saveGroupBox_layout)
        self.mainTab_layout.addWidget(self.saveGroupBox, 4,0)
        # print(f"La hauteur du groupe box: {self.saveGroupBox.height()}")
        # print(f"Le groupe box est visible? {self.saveGroupBox.isVisible()}")

    def delete_group(self):
        # print(f"La hauteur du groupe box: {self.saveGroupBox.height()}")
        # self.hideAndShow_group()
        # remove widget from the layout list
        self.mainTab_layout.removeWidget(self.saveGroupBox)
        # remove it from the gui
        self.saveGroupBox.setParent(None)
        # create new widget
        self.createSave_Box()
        # redo button connection
        self.saveButton.clicked.connect(self.savePassword)
        # refresh password box
        self.refreshPass_box()


    def exit_app(self):
        self.close()

    def refreshPass_box(self, password=""):
        self.saveGroupBox.show()
        # remove widget from the layout list
        self.mainTab_layout.removeWidget(self.pass_box)
        # remove it from the gui
        self.pass_box.setParent(None)
        # create new widget
        self.pass_box = QLineEdit()
        self.pass_box.setText(password)
        self.mainTab_layout.addWidget(self.pass_box, 2, 0, alignment=Qt.AlignCenter)

    def getPassword(self):
        newPassword = Password().get_random_password()
        print(newPassword)
        self.refreshPass_box(str(newPassword))

    def savePassword(self):
        # print(f"Le groupe box est visible? {self.saveGroupBox.isVisible()}")
        print(self.entry.text())
        print(self.entry_id.text())
        print(self.pass_box.text())
        return self.delete_group()

    def hideAndShow_group(self):
        height = self.height()
        if self.saveGroupBox.isVisible():
            height -= 150
            self.saveGroupBox.setVisible(not self.saveGroupBox.isVisible())
        else:
            height += 210
            self.saveGroupBox.setVisible(True)
        print(height)
        self.mainWindow.setFixedSize(self.width(), height)

    def animation_hideAndShow(self):
        pass