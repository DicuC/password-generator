import sys
from PyQt5 import QtWidgets
from pass_generate import PassGenerate


class PasswordGeneratorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.layout = QtWidgets.QVBoxLayout()

        self.length_label = QtWidgets.QLabel('Password Length:')
        self.layout.addWidget(self.length_label)

        self.length_entry = QtWidgets.QLineEdit()
        self.length_entry.setText('16')  # Default length set to 16
        self.layout.addWidget(self.length_entry)

        self.generate_button = QtWidgets.QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.normal_password_label = QtWidgets.QLabel('Normal Password:')
        self.layout.addWidget(self.normal_password_label)

        self.encoded_password_label = QtWidgets.QLabel('Encoded Password:')
        self.layout.addWidget(self.encoded_password_label)

        self.copy_normal_button = QtWidgets.QPushButton('Copy Normal Password')
        self.copy_normal_button.clicked.connect(self.copy_normal_to_clipboard)
        self.layout.addWidget(self.copy_normal_button)

        self.copy_encoded_button = QtWidgets.QPushButton('Copy Encoded Password')
        self.copy_encoded_button.clicked.connect(self.copy_encoded_to_clipboard)
        self.layout.addWidget(self.copy_encoded_button)

        self.setLayout(self.layout)
        self.password_generator = PassGenerate()

    def generate_password(self):
        try:
            length = int(self.length_entry.text())
            self.password_generator.set_length(length)
            normal_password, encoded_password = self.password_generator.generate_passwords()

            self.normal_password_label.setText(f'Normal Password: {normal_password}')
            self.encoded_password_label.setText(f'Encoded Password: {encoded_password}')
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, 'Error', str(e))

    def copy_normal_to_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        password_text = self.normal_password_label.text().split(': ')[1]
        clipboard.setText(password_text)
        QtWidgets.QMessageBox.information(self, 'Copied', 'Normal password copied to clipboard')

    def copy_encoded_to_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        password_text = self.encoded_password_label.text().split(': ')[1]
        clipboard.setText(password_text)
        QtWidgets.QMessageBox.information(self, 'Copied', 'Encoded password copied to clipboard')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
