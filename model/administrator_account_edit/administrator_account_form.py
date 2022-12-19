import logging

from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QTableWidgetItem, QMenu
from sqlalchemy import update

from base import Session
from cont import Cont
from views.adm_account_edit_form_view import Ui_MainWindow as AdmAccount


class AdministratorAccountManage(QtWidgets.QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.login_window = login_window
        self.UI = AdmAccount()
        self.UI.setupUi(self)
        self.data = []
        self.get_data()
        self.populate_table()
        self.table_row = []
        self.row_deleted = []
        self.UI.log_out_button.clicked.connect(self.log_out)

        self.UI.tableWidget.doubleClicked.connect(self.table_click)
        self.UI.save_button.clicked.connect(self.save_button)
        self.UI.tableWidget.installEventFilter(self)

    def save_button(self):
        try:
            for i in self.table_row:
                if i in self.row_deleted:
                    self.table_row.pop(i)
            session = Session()
            for id_cont in self.table_row:
                cont = update(Cont).where(id_cont + 1 == Cont.id).values(
                    user=self.UI.tableWidget.item(id_cont, 0).data(0),
                    parola=self.UI.tableWidget.item(id_cont, 1).data(0),
                    nivel_cont=self.UI.tableWidget.item(id_cont, 2).data(0)
                )
                session.execute(cont)
            session.commit()
            session.close()
            self.UI.tableWidget.clearContents()
            self.UI.tableWidget.clear()
            self.UI.tableWidget.clearSelection()
            self.UI.tableWidget.reset()
            self.UI.tableWidget.clearContents()
            self.data.clear()
            self.table_row.clear()
            self.row_deleted.clear()
            self.get_data()
            self.populate_table()
        except BaseException as e:
            logging.exception(e)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        try:

            if a1.type() == QEvent.ContextMenu and self.UI.tableWidget.currentRow() >= 0:
                menu = QMenu()
                menu.addAction('DELETE')
                print(self.UI.tableWidget.currentRow())
                if menu.exec_(a1.globalPos()):
                    self.delete_row()

                return True
            return super().eventFilter(a0, a1)
        except BaseException as e:
            logging.exception(e)

    def delete_row(self):
        session = Session()
        id_cont = self.UI.tableWidget.currentRow() - 1
        cont = session.query(Cont).filter(id_cont == Cont.id)

        cont.delete()

        session.commit()
        session.close()
        self.row_deleted.append(self.UI.tableWidget.currentRow())
        self.UI.tableWidget.clearContents()
        self.UI.tableWidget.clear()
        self.UI.tableWidget.clearSelection()
        self.UI.tableWidget.reset()
        self.data.clear()
        self.populate_table()


    def table_click(self):
        try:
            x = self.UI.tableWidget.currentRow()
            # row = [self.UI.tableWidget.item(x, 0).data(0),
            #        self.UI.tableWidget.item(x, 1).data(0),
            #        self.UI.tableWidget.item(x, 2).data(0), ]
            # print(x,row)
            self.table_row.append(x)

        except BaseException as e:
            logging.exception(e)

    def log_out(self):
        AdministratorAccountManage.hide(self)
        self.login_window.show()

    def get_data(self):
        try:

            session = Session()
            all_accoutns = session.query(Cont)
            for row in all_accoutns:
                item = [str(row.user), str(row.parola), str(row.nivel_cont)]
                self.data.append(item)
        except BaseException as e:
            logging.exception(e)

    def populate_table(self):
        try:
            print(self.data)
            self.UI.tableWidget.setRowCount(len(self.data))
            for idx, row in enumerate(self.data):
                self.UI.tableWidget.setItem(idx, 0, QTableWidgetItem(row[0]))
                self.UI.tableWidget.setItem(idx, 1, QTableWidgetItem(row[1]))
                self.UI.tableWidget.setItem(idx, 2, QTableWidgetItem(row[2]))
        except BaseException as e:
            logging.exception(e)
