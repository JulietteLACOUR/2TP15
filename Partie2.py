from PySide2.QtWidgets import *

class ConfigurationDialog(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")
        self.setMinimumSize(300, 100)

        self.layout = QVBoxLayout()

        self.labeledtextfield1 = LabeledTextField("IP address")
        self.labeledtextfield2 = LabeledTextField("User")
        self.labeledtextfield3 = LabeledTextField("Password")

        self.layout.addWidget(self.labeledtextfield1)
        self.layout.addWidget(self.labeledtextfield2)
        self.layout.addWidget(self.labeledtextfield3)

        self.setLayout(self.layout)



class LabeledTextField(QWidget):

    def __init__(self, text):
        QWidget.__init__(self)
        self.Text = text

        self.layout = QHBoxLayout()

        self.label1 = QLabel(text)
        self.text1 = QTextEdit()
        self.text1.setMaximumHeight(20)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.text1)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialog()
    win.show()
    app.exec_()


