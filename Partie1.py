from PySide2.QtWidgets import *
from Partie2 import *

class ButtonsPanel(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QHBoxLayout()

        self.button1 = QPushButton("Configure")
        self.button2 = QPushButton("Connect")
        self.button3 = QPushButton("Disconnect")

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)

class SQLClientWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600, 400)
        self.layout = QVBoxLayout()

        self.buttonspanel = ButtonsPanel()
        self.notificationPanel = QTextEdit()

        self.resultTable = QTableWidget(5, 3)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonspanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resultTable)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    win1 = SQLClientWindow()
    win2 = ConfigurationDialog()
    win1.show()
    win2.show()
    app.exec_()
