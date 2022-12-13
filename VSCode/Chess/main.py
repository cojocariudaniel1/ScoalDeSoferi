from PyQt5 import QtWidgets
from model.chess_window import ChesWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ChesWindow()
    widget.show()

    app.exec_()