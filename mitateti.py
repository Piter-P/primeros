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

    b4 = QtWidgets.QPushButton(win)
    b4.setGeometry(QtCore.QRect(10, 110, 90, 90))
    b4.setFont(font)
    b4.setText('4')

    b5 = QtWidgets.QPushButton(win)
    b5.setGeometry(QtCore.QRect(110, 110, 90, 90))
    b5.setFont(font)
    b5.setText('5')

    b6 = QtWidgets.QPushButton(win)
    b6.setGeometry(QtCore.QRect(210, 110, 90, 90))
    b6.setFont(font)
    b6.setText('6')

    b7 = QtWidgets.QPushButton(win)
    b7.setGeometry(QtCore.QRect(10, 210, 90, 90))
    b7.setFont(font)
    b7.setText('7')

    b8 = QtWidgets.QPushButton(win)
    b8.setGeometry(QtCore.QRect(110, 210, 90, 90))
    b8.setFont(font)
    b8.setText('8')

    b9 = QtWidgets.QPushButton(win)
    b9.setGeometry(QtCore.QRect(210, 210, 90, 90))
    b9.setFont(font)
    b9.setText('9')

    label = QtWidgets.QLabel(win)
    label.setText('probando ')
    label.move(10,325)

    win.show()
    app.exec_()

ventana()
