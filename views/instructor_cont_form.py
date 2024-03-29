# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructor_cont_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_background = QtWidgets.QLabel(self.centralwidget)
        self.image_background.setGeometry(QtCore.QRect(-80, -10, 1061, 621))
        self.image_background.setStyleSheet("background-color: rgb(0, 0, 70);")
        self.image_background.setText("")
        self.image_background.setObjectName("image_background")
        self.user_name_account_s = QtWidgets.QLabel(self.centralwidget)
        self.user_name_account_s.setGeometry(QtCore.QRect(105, 0, 671, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.user_name_account_s.setFont(font)
        self.user_name_account_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 24pt \"Arial Black\";")
        self.user_name_account_s.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_account_s.setWordWrap(True)
        self.user_name_account_s.setObjectName("user_name_account_s")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(205, 125, 226, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.vehicul_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.vehicul_label.setFont(font)
        self.vehicul_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.vehicul_label.setObjectName("vehicul_label")
        self.gridLayout.addWidget(self.vehicul_label, 2, 0, 1, 1)
        self.prenume_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prenume_label.setFont(font)
        self.prenume_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.prenume_label.setObjectName("prenume_label")
        self.gridLayout.addWidget(self.prenume_label, 1, 0, 1, 1)
        self.nume_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nume_label.setFont(font)
        self.nume_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nume_label.setObjectName("nume_label")
        self.gridLayout.addWidget(self.nume_label, 0, 0, 1, 1)
        self.nr_inamtriculare_label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nr_inamtriculare_label.setFont(font)
        self.nr_inamtriculare_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nr_inamtriculare_label.setObjectName("nr_inamtriculare_label")
        self.gridLayout.addWidget(self.nr_inamtriculare_label, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-125, 415, 1071, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-40, 85, 1071, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.programari_button = QtWidgets.QPushButton(self.centralwidget)
        self.programari_button.setGeometry(QtCore.QRect(20, 455, 251, 61))
        self.programari_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.programari_button.setObjectName("programari_button")
        self.log_out_2 = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_2.setGeometry(QtCore.QRect(680, 450, 141, 61))
        self.log_out_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 16pt \"Arial\";\n"
"")
        self.log_out_2.setObjectName("log_out_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(470, 125, 226, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.prenume_s = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prenume_s.setFont(font)
        self.prenume_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.prenume_s.setObjectName("prenume_s")
        self.gridLayout_2.addWidget(self.prenume_s, 1, 0, 1, 1)
        self.vehicul_s = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.vehicul_s.setFont(font)
        self.vehicul_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.vehicul_s.setObjectName("vehicul_s")
        self.gridLayout_2.addWidget(self.vehicul_s, 2, 0, 1, 1)
        self.nr_imatriculare_s = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nr_imatriculare_s.setFont(font)
        self.nr_imatriculare_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nr_imatriculare_s.setObjectName("nr_imatriculare_s")
        self.gridLayout_2.addWidget(self.nr_imatriculare_s, 3, 0, 1, 1)
        self.nume_s = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nume_s.setFont(font)
        self.nume_s.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.nume_s.setObjectName("nume_s")
        self.gridLayout_2.addWidget(self.nume_s, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_name_account_s.setText(_translate("MainWindow", "user_name_account"))
        self.vehicul_label.setText(_translate("MainWindow", "Vehicul"))
        self.prenume_label.setText(_translate("MainWindow", "Prenume"))
        self.nume_label.setText(_translate("MainWindow", "Nume"))
        self.nr_inamtriculare_label.setText(_translate("MainWindow", "Numar inmatriculare"))
        self.programari_button.setText(_translate("MainWindow", "Programari"))
        self.log_out_2.setText(_translate("MainWindow", "Log out"))
        self.prenume_s.setText(_translate("MainWindow", "NULL"))
        self.vehicul_s.setText(_translate("MainWindow", "NULL"))
        self.nr_imatriculare_s.setText(_translate("MainWindow", "NULL"))
        self.nume_s.setText(_translate("MainWindow", "NULL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
