from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import Session
from sqlalchemy import select

from cont import Cont
from personal import Personal
from instructor import Instructor
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre

from base import Session
from cont import Cont
from views.cont_form_view import Ui_MainWindow as ContForm
from model.achizitioneaza_ore_form.achizitoneaza_ore_form import AchizitoneazaOreWindow


class ContWindow(QtWidgets.QMainWindow):
    def __init__(self, username = None):
        super().__init__()

        self.new_window = None
        self.UI = ContForm()
        self.UI.setupUi(self)

        self.username = username
        self.get_info(self.username)

        self.UI.achizitioneaza_ore_button.clicked.connect(self.achizitoneaza_ore_form)

    def achizitoneaza_ore_form(self):
        ContWindow.hide(self)
        self.new_window = AchizitoneazaOreWindow()
        self.new_window.show()

    def get_info(self, username):
        session = Session()
        query = session.query(Cont).filter(Cont.user == username)
        for cont in query:
            if cont.nivel_cont == 0:
                cursant_query = session.query(Cursant).filter(Cursant.cont_id == cont.id)
                for item in cursant_query:
                    pass
                    try:
                        self.UI.nume_s.setText(item.nume)
                        self.UI.prenume_s.setText(item.prenume)
                        self.UI.dataNasterii_s.setText(str(item.dataNasterii))
                    except Exception as e:
                        print(e)
            elif cont.nivel_cont == 1:
                pass
            elif cont.nivel_cont == 2:
                pass
