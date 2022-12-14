from time import strftime

from PyQt5 import QtCore
from PyQt5 import QtWidgets

from base import Session
from cont import Cont
from instructor import Instructor
from model.instructor_cont_form.instructor_programari import InstructorProgramari
from personal import Personal
from vehicul import Vehicul
from views.instructor_cont_form import Ui_MainWindow


class InstructorContForm(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()

        self.new_window = None
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.username = username
        self.get_info(self.username)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(2000)
        self.UI.programari_button.clicked.connect(self.programari_button)

    def programari_button(self):
        self.new_window = InstructorProgramari(self.username)
        self.new_window.show()
        self.get_info(self.username)

    def Time(self):
        if int(strftime("%S")) % 10 == 0:
            self.timer.setInterval(2000)
        else:
            self.timer.setInterval(2000)
        self.get_info(self.username)
        try:
            pass
            # if int(self.UI.oreDisponibile_s.text()):
            #     print('test')
            # if int(self.UI.oreDisponibile_s.text()) != 0:
            #     self.UI.programare_button.setDisabled(False)
            # else:
            #     self.UI.programare_button.setDisabled(True)
        except Exception as e:
            print(e)

    def get_info(self, username):
        session = Session()
        query = session.query(Cont).filter(Cont.user == username)

        for cont in query:
            if cont.nivel_cont == 1:
                instructor = session.query(Instructor).filter(Instructor.cont_id == cont.id).first()
                personal = session.query(Personal).filter(Personal.id == instructor.id)
                vehicul = session.query(Vehicul).filter(Vehicul.id == instructor.vehicul_id).first()
                for item in personal:
                    self.UI.user_name_account_s.setText(self.username)
                    self.personal_id = item.id
                    self.UI.nume_s.setText(item.nume)
                    self.UI.prenume_s.setText(item.prenume)
                    self.UI.vehicul_s.setText(vehicul.marca)
                    self.UI.nr_imatriculare_s.setText(vehicul.numar_de_inmatriculare)
