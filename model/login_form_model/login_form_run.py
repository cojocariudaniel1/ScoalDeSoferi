import logging

from PyQt5 import QtWidgets

from base import Session
from cont import Cont
from model.instructor_cont_form.instructor_cont_form import InstructorContForm
from model.user_account_form.user_form_run import ContWindow
from views.login_form_view import Ui_Form


class LoginWndow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.new_window = None
        self.ui_loginForm = Ui_Form()
        self.ui_loginForm.setupUi(self)

        self.ui_loginForm.login_button.clicked.connect(self.login_check)

    def login_check(self):
        try:
            username = self.ui_loginForm.username_input.text()
            password = self.ui_loginForm.password_input.text()
            session = Session()
            query = session.query(Cont).filter(Cont.user == username, Cont.parola == password)
            count = 0
            for row in query:
                if row.user:
                    count += 1
            if count == 1:
                query = session.query(Cont).filter(Cont.user == username)

                for cont in query:
                    if cont.nivel_cont == 0:
                        LoginWndow.hide(self)
                        self.new_window = ContWindow(username)
                        self.new_window.show()
                    elif cont.nivel_cont == 1:
                        LoginWndow.hide(self)
                        self.new_window = InstructorContForm(username)
                        self.new_window.show()
            else:
                print("Failed")
            session.commit()
            session.close()
        except BaseException as e:
            logging.exception(e)
