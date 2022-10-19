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
from views.achizitonare_ore_view import Ui_MainWindow


class AchizitoneazaOreWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
