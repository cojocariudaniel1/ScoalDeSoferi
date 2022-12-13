
import logging
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QDrag,QPixmap,QPainter, QImage
from PyQt5.QtCore import Qt,QMimeData
from PyQt5.QtWidgets import QLabel, QGridLayout, QApplication
from views.ui_chess import Ui_Form
from model.sprites_func import chess_table, pieces
import uuid
import psutil

initiate_matrix = [
    [-50, -30, -40, -9, -10, -41, -31, -51],
    [-11, -12, -13, -14, -15, -16, -17, -18],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [11, 12, 13, 14, 15, 16, 17, 18],
    [50, 30, 40, 9, 10, 41, 31, 51]
]



class ChesWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.list_pieces = []

        self.UI = Ui_Form()
        self.UI.setupUi(self)
    

        self.UI.pushButton.clicked.connect(self.button)
        self.UI.pushButton_2.clicked.connect(self.reload)
        self.draw_chess_board()
        self.draw_pieces_on_table()
        self.drag_position = None

    def reload(self):   
        self.draw_chess_board()
        self.draw_pieces_on_table()




    def draw_pieces_on_table(self):
        x = 0
        y = 0
        for idx_row, row in enumerate(initiate_matrix):
            for idx_column, column in enumerate(row):
                if column != 0:
                    y = idx_row * 100 + 13
                    x = idx_column * 100 + 13
                    id = uuid.uuid1()
                    item = self.piece(x,y, pieces(column),id.int)
                    item.show()
                    self.list_pieces.append(item)
      
    def button(self):
        for i in reversed(range(self.UI.chess_grid.count())):
            self.UI.chess_grid.itemAt(i).widget().setParent(None)

        for i in self.list_pieces:
            # i.deleteLater()
            i.deleteLater() # lets Qt knows it needs to delete this widget from the GUI
            del i
        self.list_pieces.clear()

    def piece(self, x,y, img, name):
        piece = QtWidgets.QLabel(self)
        piece.setGeometry(QtCore.QRect(x, y, 70, 70))
        piece.setPixmap(QtGui.QPixmap(img).scaled(70, 70, QtCore.Qt.KeepAspectRatio)) 
        piece.setObjectName(f"{name}")
        piece.setAlignment(QtCore.Qt.AlignCenter)
        return piece

    def draw_chess_board(self):
        square = chess_table()
        temp = 0
        for idx_row,row in enumerate(initiate_matrix):
            for idx_column, column in enumerate(row):
                if idx_row % 2 == 0:
                    if temp == 0:
                        self.UI.chess_grid.addWidget(self.square(square[0]), idx_row, idx_column)
                        temp = 1
                    else:
                        self.UI.chess_grid.addWidget(self.square(square[1]), idx_row, idx_column)
                        temp = 0
                else:
                    if temp == 0:
                        self.UI.chess_grid.addWidget(self.square(square[1]), idx_row, idx_column)
                        temp = 1
                    else:
                        self.UI.chess_grid.addWidget(self.square(square[0]), idx_row, idx_column)
                        temp = 0                    

 

        self.UI.chess_grid.setHorizontalSpacing(0)
        self.UI.chess_grid.setVerticalSpacing(0)
    def square(self, img):
        square = QtWidgets.QLabel()
        square.setPixmap(QtGui.QPixmap(img).scaled(100, 100, QtCore.Qt.KeepAspectRatio)) 
        square.setObjectName("label")
        square.setAlignment(QtCore.Qt.AlignCenter)
        return square