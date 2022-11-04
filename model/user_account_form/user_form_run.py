import sys
from time import strftime
import time

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from base import Session
from sqlalchemy import select

from cont import Cont
from model.programare_form.programare_form_run import ProgramareWindow
from personal import Personal
from instructor import Instructor
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre
from personal_administrativ import PersonalAdministrativ
from base import Session
from cont import Cont
from views.cont_form_view import Ui_MainWindow as ContForm
from model.achizitioneaza_ore_form.achizitoneaza_ore_form import AchizitoneazaOreWindow


class ContWindow(QtWidgets.QMainWindow):
    def __init__(self, username = None):
        super().__init__()
        self.ore = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)

        self.new_window = None
        self.UI = ContForm()
        self.UI.setupUi(self)
        self.username = username
        self.cursant_id = None
        self.get_info(self.username)

        self.UI.achizitioneaza_ore_button.clicked.connect(self.achizitoneaza_ore_form)
        self.UI.programare_button.clicked.connect(self.programare_form)
        self.UI.log_out.clicked.connect(self.log_out)

    def log_out(self):
        sys.exit()

    def Time(self):
        if int(strftime("%S")) % 10 == 0:
            self.timer.setInterval(1000)
        else:
            self.timer.setInterval(1000)
        self.get_info(self.username)
        try:

            if int(self.UI.oreDisponibile_s.text()) != 0:
                self.UI.programare_button.setDisabled(False)
            else:
                self.UI.programare_button.setDisabled(True)
        except Exception as e:
            print(e)
        if self.ore == 0:
            self.UI.achizitioneaza_ore_button.setDisabled(False)
        else:
            self.UI.achizitioneaza_ore_button.setDisabled(True)


    def programare_form(self):
        try:
            self.new_window = ProgramareWindow(self.username)
            self.new_window.show()
        except Exception as e:
            print(e)


    def achizitoneaza_ore_form(self):
        self.new_window = AchizitoneazaOreWindow(self.cursant_id, self.username)
        self.new_window.show()
        self.get_info(self.username)

    def get_info(self, username):
        session = Session()
        query = session.query(Cont).filter(Cont.user == username)
        for cont in query:
            if cont.nivel_cont == 0:
                cursant_query = session.query(Cursant).filter(Cursant.cont_id == cont.id)
                for item in cursant_query:
                    pass
                    try:
                        self.cursant_id = item.id
                        self.UI.nume_s.setText(item.nume)
                        self.UI.prenume_s.setText(item.prenume)
                        self.UI.dataNasterii_s.setText(str(item.dataNasterii))
                        self.UI.oreDisponibile_s.setText(str(item.nr_ore))
                        self.UI.label_10.setText(str(item.ore_finalizate))
                        self.UI.user_name_account_s.setText(str(cont.user.upper()))

                        self.ore = int(item.nr_ore)
                    except Exception as e:
                        print(e)
            elif cont.nivel_cont == 1:
                pass
            elif cont.nivel_cont == 2:
                pass
