import sys
from window import Ui
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
