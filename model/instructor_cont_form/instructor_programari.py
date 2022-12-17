import logging
from datetime import datetime

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from sqlalchemy import update

from base import Session
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from personal import Personal
from programare import Programare
from views.programari_instructor import Ui_MainWindow


def check_ora(y):
    ora = None
    if y == 1:
        ora = 8
    elif y == 2:
        ora = 10
    elif y == 3:
        ora = 12
    elif y == 4:
        ora = 14
    elif y == 5:
        ora = 16
    elif y == 6:
        ora = 18
    return ora


class InstructorProgramari(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()

        self.date_object = None
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.table_cord = []
        self.data = []
        self.username = username
        self.last_cell = [0, 0]
        self.populate_tabel()
        self.instructor_id = None
        self.cursant_id = None
        self.data_update_tabel()
        self.UI.programareTableWidget.clicked.connect(self.table_click)
        self.UI.confirma_ora_button.clicked.connect(self.programare_button)
        self.UI.update_table_button.clicked.connect(self.data_update_tabel)

    def data_update_tabel(self):
        try:
            string_data = str(self.UI.dateEdit.text()).replace("/", "-")
            print(string_data)

            self.populate_tabel(string_data)

        except BaseException as e:
            logging.exception(e)

    def populate_tabel(self, string_data='NULL'):
        try:
            self.data.clear()
            self.table_cord.clear()
            session = Session()
            programari = None

            # Query pentru a primi numele si prenumele de la cursant.
            cont = session.query(Cont).where(Cont.user == self.username).first()

            ###

            # Query petnru a primi numele la personal
            instructor = session.query(Instructor).filter(Instructor.cont_id == cont.id).first()
            personal = session.query(Personal).where(Personal.id == instructor.personal_id).first()
            self.UI.instructor_label_s.setText(f"{str(personal.nume)} {str(personal.prenume)}")
            self.instructor_id = instructor.id
            ###

            # Conditie pentru a vedea daca data a fost schimbata de catre cursant
            if string_data == 'NULL':

                programari = session.query(Programare).order_by(Programare.data).where(
                    Programare.instructor_id == self.instructor_id)
            else:
                date_object = datetime.strptime(string_data, '%Y-%m-%d').date()
                programari = session.query(Programare).order_by(Programare.data). \
                    where(Programare.data >= date_object,
                          Programare.instructor_id == self.instructor_id)

            # Curatare tabel inainte de popularea acestuia
            self.UI.programareTableWidget.clearContents()

            # Metoda de a vedea nr de programari fara a se repeta zilele
            count = 0
            last_data = None
            for i in programari:
                if last_data != i.data:
                    last_data = i.data
                    count += 1
            # Setare nr de randuri in functie de numarul de programari
            self.UI.programareTableWidget.setRowCount(count)

            # Colorare celule din tabel cu verde
            for idx, row in enumerate(programari):
                self.color_cell_green(idx, 1)
                self.color_cell_green(idx, 2)
                self.color_cell_green(idx, 3)
                self.color_cell_green(idx, 4)
                self.color_cell_green(idx, 5)
                self.color_cell_green(idx, 6)

            # Tinem cont de valoarea anterioara a datei pentru a nu se adauga un rand nou in tabel.
            temp = None
            index_track = 0

            # Adaugare prima programare. Pentru a avea ultima data.
            for row in programari:
                temp = row.data
                self.data.append([row.id, row.data, row.ora, row.cursant_id, row.instructor_id])
                self.UI.programareTableWidget.setItem(index_track, 0, QTableWidgetItem(str(row.data)))
                break
            print(temp)

            # Adaugare restul de programari in functie daca se repeta sau nu datele
            for row in programari:
                if row.data != temp:
                    index_track += 1
                    temp = row.data
                    # Adaugare date in lista pentru a verifica pe urma daca cursatul se programeaza intr-o zi libera
                    self.data.append([row.id, row.data, row.ora, row.cursant_id, row.instructor_id])

                    # Adaugare rand cu data respectiva
                    self.UI.programareTableWidget.setItem(index_track, 0, QTableWidgetItem(str(row.data)))

                    # Colorare rand cu rosu deoarece este ocupat
                    self.color_table(row, index_track)

                else:
                    # Doar se coloreaza randul si nu se adauga un rand nou (Pentru a nu se crea un rand nou pentru
                    # fiecare ora in parte
                    self.data.append([row.id, row.data, row.ora, row.cursant_id, row.instructor_id])
                    self.color_table(row, index_track)
        except BaseException as e:
            logging.exception(e)

    # Functie de colorare cu rosu casutelor din tabel.
    def color_table(self, row, index_track):
        try:
            if row.ora == 8:
                self.color_cell_red(index_track, 1)
                self.table_cord.append([index_track, 1])
            elif row.ora == 10:
                self.color_cell_red(index_track, 2)
                self.table_cord.append([index_track, 2])

            elif row.ora == 12:
                self.color_cell_red(index_track, 3)
                self.table_cord.append([index_track, 3])

            elif row.ora == 14:
                self.color_cell_red(index_track, 4)
                self.table_cord.append([index_track, 4])

            elif row.ora == 16:
                self.color_cell_red(index_track, 5)
                self.table_cord.append([index_track, 5])

            elif row.ora == 18:
                self.color_cell_red(index_track, 6)
                self.table_cord.append([index_track, 6])
        except BaseException as e:
            logging.exception(e)

    # Functia de colorare cu rosu
    def color_cell_red(self, x, y):
        try:
            item = QtWidgets.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(255, 15, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            self.UI.programareTableWidget.setItem(x, y, item)
        except BaseException as e:
            logging.exception(e)

    # Functia de colorare cu verde
    def color_cell_green(self, x, y):
        try:
            item = QtWidgets.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(124, 252, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            self.UI.programareTableWidget.setItem(x, y, item)
        except BaseException as e:
            logging.exception(e)

    # Functia de verificare daca cursantul a dat click pe o casuta din tabel.
    def table_click(self):
        try:
            self.last_cell.clear()
            x = self.UI.programareTableWidget.currentRow()
            y = self.UI.programareTableWidget.currentColumn()
            data = self.UI.programareTableWidget.item(x, 0).data(0)
            print(type(data))
            self.last_cell.append(x)
            self.last_cell.append(y)
            self.last_cell.append(data)
            print(self.last_cell)
        except BaseException as e:
            logging.exception(e)

    def programare_button(self):
        try:
            x, y = self.last_cell[0], self.last_cell[1]
            self.date_object = datetime.strptime(str(self.last_cell[2]), '%Y-%m-%d').date()
            session = Session()

            for row in self.data:
                if row[1] == self.date_object:
                    if [x, y] in self.table_cord:
                        ora = check_ora(y)
                        programari = session.query(Programare).filter(Programare.data == self.date_object,
                                                                      Programare.ora == ora)
                        cursant = session.query(Cursant).filter(Cursant.id == programari[0].cursant_id).first()
                        update_cursant_ore_disponibile = update(Cursant).where(
                            Cursant.id == programari[0].cursant_id).values(nr_ore=cursant.nr_ore - 2)
                        update_cursant_ore_finalizate = update(Cursant).where(
                            Cursant.id == programari[0].cursant_id).values(ore_finalizate=cursant.ore_finalizate + 2)

                        programari.delete()

                        session.execute(update_cursant_ore_disponibile)
                        session.execute(update_cursant_ore_finalizate)
                        session.commit()
                        session.close()
                        self.populate_tabel()
                        print('Confirma ora')
        except BaseException as e:
            logging.exception(e)
