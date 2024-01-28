from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


def ventana():
    font = QtGui.QFont()
    font.setPointSize(25)
    app = QApplication([])
    win = QMainWindow()
    win.setWindowTitle('TATETI')
    win.resize(310, 400)
    
    b1 = QtWidgets.QPushButton(win)
    b1.setGeometry(QtCore.QRect(10, 10, 90, 90))
    b1.setFont(font)
    b1.setText('1')


    b2 = QtWidgets.QPushButton(win)
    b2.setGeometry(QtCore.QRect(110, 10, 90, 90))
    b2.setFont(font)
    b2.setText('2')

    b3 = QtWidgets.QPushButton(win)
    b3.setGeometry(QtCore.QRect(210, 10, 90, 90))
    b3.setFont(font)
    b3.setText('3')

    win.show()
    app.exec_()

ventana()
