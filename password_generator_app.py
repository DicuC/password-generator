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

        self.copy_button = QtWidgets.QPushButton('Copy to Clipboard')
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.layout.addWidget(self.copy_button)

        self.result_label = QtWidgets.QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.password_generator = PassGenerate()

    def generate_password(self):
        try:
            length = int(self.length_entry.text())
            self.password_generator.set_length(length)
            password = self.password_generator.generate()
            self.result_label.setText(f'Generated Password: {password}')
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, 'Error', str(e))

    def copy_to_clipboard(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.result_label.text().split(': ')[1])
        QtWidgets.QMessageBox.information(self, 'Copied', 'Password copied to clipboard')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())