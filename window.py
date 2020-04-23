from calculator import Calculator
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('window.ui', self)

        self.initializeWidgets()
        self.button.clicked.connect(self.calculateButtonOnClick)

    def initializeWidgets(self):
        self.button = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.textArea = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.label = self.findChild(QtWidgets.QLabel, 'label')
        self.addition = self.findChild(QtWidgets.QRadioButton, 'radioButton')
        self.multiplication = self.findChild(QtWidgets.QRadioButton, 'radioButton_2')

    def calculateButtonOnClick(self):
        calculator = Calculator()
        result = 0
        if self.addition.isChecked():
            result = calculator.add(self.textArea.toPlainText())
        elif self.multiplication.isChecked():
            result = calculator.multiply(self.textArea.toPlainText())
        self.label.setText("Result: {}".format(str(result)))
