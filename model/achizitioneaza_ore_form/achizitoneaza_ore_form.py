import logging

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from base import Session
from sqlalchemy import select, update

from cont import Cont
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
from views.achizitionare_ore import Ui_MainWindow
from PyQt5.QtCore import Qt, pyqtSignal


class AchizitoneazaOreWindow(QtWidgets.QMainWindow):
    def __init__(self, cursant_id, username):
        super().__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)

        self.username = username
        self.cursant_id = cursant_id
        print(self.cursant_id)
        self.new_window = None
        self.table_row = []
        self.UI.tableWidget.clicked.connect(self.table_click)
        self.UI.manualRB.clicked.connect(self.filter_by_manualRB)
        self.UI.automatRB.clicked.connect(self.filter_by_automatRB)
        self.data_achizitonare = []
        self.get_data()
        self.populate_tabel(self.data_achizitonare)
        self.UI.achizitioneaza_button.clicked.connect(self.achizitoneaza_buton)

        self.filter_list = []

    def achizitoneaza_buton(self):
        try:
            nume_prenume = self.table_row[0].split()
            nume, prenume = nume_prenume[0], nume_prenume[1]
            vehicul = self.table_row[1]
            numar_inmatriculare = self.table_row[2]
            pachet_ore = self.table_row[4]
            pret = self.table_row[5]

            session = Session()
            personal = session.query(Personal).filter(Personal.nume == nume, Personal.prenume == prenume).first()
            instructor = session.query(Instructor).filter(Instructor.personal_id == personal.id, ).first()
            pachet_ore_relation_ship = session.query(PachetOre.instructor_pachet_ore_relationship)
            for row in pachet_ore_relation_ship:
                if row[0] == instructor.id:
                    update_pachet_ore = update(Cursant).where(Cursant.id == self.cursant_id).values(
                        pachet_ore_id=row[1], nr_ore=pachet_ore, instructor_id=instructor.id)
                    session.execute(update_pachet_ore)
                    session.commit()
                    session.close()
                    QMessageBox.about(self, "Achizitionare ore", "Succes")
                    AchizitoneazaOreWindow.hide(self)
                    break

        except BaseException as e:
            logging.exception(e)

    def populate_tabel(self, data):
        # columns -> 0: instructor, 1: vehicul, 2: nr inmatriculare, 3: cutia vit, 4: ore, 5: pret
        try:
            for idx, row in enumerate(data):
                self.UI.tableWidget.setItem(idx, 0, QTableWidgetItem(row[2]))
                self.UI.tableWidget.setItem(idx, 1, QTableWidgetItem(row[3]))
                self.UI.tableWidget.setItem(idx, 2, QTableWidgetItem(row[4]))
                self.UI.tableWidget.setItem(idx, 3, QTableWidgetItem(row[5]))
                self.UI.tableWidget.setItem(idx, 4, QTableWidgetItem(str(row[0])))
                self.UI.tableWidget.setItem(idx, 5, QTableWidgetItem(str(row[1])))
        except BaseException as e:
            logging.exception(e)

    def filter_by_automatRB(self):
        try:
            self.filter_list.clear()
            self.data_achizitonare.clear()
            self.get_data()
            for idx, row in enumerate(self.data_achizitonare):
                if row[5] == "Automat":
                    self.filter_list.append(row)
            self.UI.tableWidget.clearContents()
            self.populate_tabel(self.filter_list)
            print(self.data_achizitonare)
        except BaseException as e:
            logging.exception(e)

    def filter_by_manualRB(self):
        try:
            self.filter_list.clear()
            self.data_achizitonare.clear()
            self.get_data()
            for idx, row in enumerate(self.data_achizitonare):
                if row[5] == "Manual":
                    self.filter_list.append(row)
            print(self.data_achizitonare)
            self.UI.tableWidget.clearContents()
            self.populate_tabel(self.filter_list)
        except BaseException as e:
            logging.exception(e)

    def get_data(self):
        try:
            # 0: ore, 1: pret, 2: nume, 3: marca, 4: numar inm, 5: cutie de viteze
            session = Session()
            pachet_ore_relation = session.query(PachetOre.instructor_pachet_ore_relationship)
            for row in pachet_ore_relation:
                items = []
                pachet_ore = session.query(PachetOre).filter(PachetOre.id == row[1])
                instructor = session.query(Instructor).filter(Instructor.id == row[0])
                for k in pachet_ore:
                    items.append(k.durata)
                    items.append(k.pret)
                for k in instructor:
                    personal = session.query(Personal).filter(Personal.id == k.personal_id)
                    for row in personal:
                        personal_name = f"{row.nume} {row.prenume}"
                        items.append(personal_name)
                    vehicul = session.query(Vehicul).filter(Vehicul.id == k.vehicul_id)
                    for row in vehicul:
                        items.append(row.marca)
                        items.append(row.numar_de_inmatriculare)
                        items.append(row.cutie_de_viteze)
                self.data_achizitonare.append(items)
            print(self.data_achizitonare)
            session.close()
        except BaseException as e:
            logging.exception(e)

    def table_click(self):
        try:
            self.table_row.clear()
            x = self.UI.tableWidget.currentRow()

            row = [self.UI.tableWidget.item(x, 0).data(0),
                   self.UI.tableWidget.item(x, 1).data(0),
                   self.UI.tableWidget.item(x, 2).data(0),
                   self.UI.tableWidget.item(x, 3).data(0),
                   self.UI.tableWidget.item(x, 4).data(0),
                   self.UI.tableWidget.item(x, 5).data(0)]

            for item in row:
                self.table_row.append(item)
        except BaseException as e:
            logging.exception(e)
