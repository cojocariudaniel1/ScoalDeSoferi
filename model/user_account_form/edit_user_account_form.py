import logging
import datetime
from time import strftime

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy import update

from base import Session
from cont import Cont
from cursant import Cursant
from views.edit_cont_form_view import Ui_MainWindow as ContForm


class EditeazaContWindow(QtWidgets.QMainWindow):
    def __init__(self, username="", ):
        super().__init__()
        self.ore = 0
        self.new_window = None
        self.UI = ContForm()
        self.UI.setupUi(self)
        self.username = username
        self.get_info(self.username)

        self.cursant_id = None
        self.UI.cancel_button.clicked.connect(self.close_window)
        self.UI.save_button.clicked.connect(self.save_data)

    def close_window(self):
        EditeazaContWindow.hide(self)

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            QMessageBox.critical(self, "Date error", "Incorrect data format, should be YYYY-MM-DD")
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def validate_input(self):
        input_list = [self.UI.nume_input, self.UI.prenume_input, self.UI.data_nasterii_input]
        for item in input_list:
            if len(item.text()) < 1:
                QMessageBox.critical(self, "Value is NULL", "The value cannot be empty")
                raise ValueError("The value cannot be empty")


    def save_data(self):
        try:
            self.validate_input()
            self.validate_date(self.UI.data_nasterii_input.text())
            session = Session()
            cont_cursant = session.query(Cont).filter(Cont.user == self.username).first()
            update_cursant = update(Cursant).where(
                Cursant.cont_id == cont_cursant.id
            ).values(nume=str(self.UI.nume_input.text()),
                     dataNasterii=str(self.UI.data_nasterii_input.text()),
                     prenume=str(self.UI.prenume_input.text()))
            # update_cursant_prenume = update(Cursant).where(
            #     Cursant.cont_id == cont_cursant.id
            # ).values()
            # update_cursant_data_nasterii = update(Cursant).where(
            #     Cursant.cont_id == cont_cursant.id
            # ).values()
            session.execute(update_cursant)
            session.commit()
            session.close()

            EditeazaContWindow.hide(self)
        except BaseException as e:
            logging.exception(e)

    def get_info(self, username):
        session = Session()
        query = session.query(Cont).filter(Cont.user == username)

        for cont in query:
            if cont.nivel_cont == 0:
                cursant_query = session.query(Cursant).filter(Cursant.cont_id == cont.id)
                for item in cursant_query:
                    try:
                        self.cursant_id = item.id
                        self.UI.nume_input.setText(item.nume)
                        self.UI.prenume_input.setText(item.prenume)
                        self.UI.data_nasterii_input.setText(str(item.dataNasterii))
                        self.UI.user_name_account_s.setText(str(cont.user.upper()))

                        self.ore = int(item.nr_ore)
                    except Exception as e:
                        print(e)
                # verificare daca cursantul este programat.
