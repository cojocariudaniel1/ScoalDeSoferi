# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'achizitionare_ore.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login_titlu_label = QtWidgets.QLabel(self.centralwidget)
        self.login_titlu_label.setGeometry(QtCore.QRect(5, -5, 1061, 91))
        self.login_titlu_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 25pt \"Arial Black\";")
        self.login_titlu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_titlu_label.setObjectName("login_titlu_label")
        self.achizitioneaza_button = QtWidgets.QPushButton(self.centralwidget)
        self.achizitioneaza_button.setGeometry(QtCore.QRect(615, 515, 211, 71))
        self.achizitioneaza_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.achizitioneaza_button.setObjectName("achizitioneaza_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(35, 515, 305, 77))
        self.layoutWidget.setObjectName("layoutWidget")
        self.cutieDeVitezeLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.cutieDeVitezeLayout.setContentsMargins(0, 0, 0, 0)
        self.cutieDeVitezeLayout.setObjectName("cutieDeVitezeLayout")
        self.automatRB = QtWidgets.QRadioButton(self.layoutWidget)
        self.automatRB.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.automatRB.setObjectName("automatRB")
        self.cutieDeVitezeLayout.addWidget(self.automatRB, 1, 0, 1, 1)
        self.manualRB = QtWidgets.QRadioButton(self.layoutWidget)
        self.manualRB.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.manualRB.setObjectName("manualRB")
        self.cutieDeVitezeLayout.addWidget(self.manualRB, 1, 1, 1, 1)
        self.cutie_de_viteza_label = QtWidgets.QLabel(self.layoutWidget)
        self.cutie_de_viteza_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.cutie_de_viteza_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cutie_de_viteza_label.setObjectName("cutie_de_viteza_label")
        self.cutieDeVitezeLayout.addWidget(self.cutie_de_viteza_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(25, 85, 1011, 401))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.image_background = QtWidgets.QLabel(self.centralwidget)
        self.image_background.setGeometry(QtCore.QRect(-15, -45, 1106, 676))
        self.image_background.setStyleSheet("background-color: rgb(0, 0, 70);")
        self.image_background.setText("")
        self.image_background.setObjectName("image_background")
        self.image_background.raise_()
        self.login_titlu_label.raise_()
        self.achizitioneaza_button.raise_()
        self.layoutWidget.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_titlu_label.setText(_translate("MainWindow", "Achizitonare ore"))
        self.achizitioneaza_button.setText(_translate("MainWindow", "Achizitioneaza"))
        self.automatRB.setText(_translate("MainWindow", "Automat"))
        self.manualRB.setText(_translate("MainWindow", "Manual"))
        self.cutie_de_viteza_label.setText(_translate("MainWindow", "Cutie de viteza"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instructor"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vehicul"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Numar Inmatriculare"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cutia de viteze"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pachet ore"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Pret"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Florin Lupascu Leonard"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Audi"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "ERB 538"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "Automata"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "30"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "200 RON"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Andrei"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Dacia"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "AER 723"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "Manuala"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "100 RON"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
