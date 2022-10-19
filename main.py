from PyQt5 import QtWidgets

from model.login_form_model.login_form_run import LoginWndow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = LoginWndow()
    widget.show()

    app.exec_()