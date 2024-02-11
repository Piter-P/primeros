from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

class MiVentana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('TATETI')
        self.resize(310, 400)
        self.graficos()


    def graficos(self):
        font = QtGui.QFont()
        font.setPointSize(25)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(QtCore.QRect(10, 10, 90, 90))
        self.b1.setFont(font)
        self.b1.setText('1')


        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setGeometry(QtCore.QRect(110, 10, 90, 90))
        self.b2.setFont(font)
        self.b2.setText('2')

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setGeometry(QtCore.QRect(210, 10, 90, 90))
        self.b3.setFont(font)
        self.b3.setText('3')

        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setGeometry(QtCore.QRect(10, 110, 90, 90))
        self.b4.setFont(font)
        self.b4.setText('4')

        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setGeometry(QtCore.QRect(110, 110, 90, 90))
        self.b5.setFont(font)
        self.b5.setText('5')

        self.b6 = QtWidgets.QPushButton(self)
        self.b6.setGeometry(QtCore.QRect(210, 110, 90, 90))
        self.b6.setFont(font)
        self.b6.setText('6')

        self.b7 = QtWidgets.QPushButton(self)
        self.b7.setGeometry(QtCore.QRect(10, 210, 90, 90))
        self.b7.setFont(font)
        self.b7.setText('7')

        self.b8 = QtWidgets.QPushButton(self)
        self.b8.setGeometry(QtCore.QRect(110, 210, 90, 90))
        self.b8.setFont(font)
        self.b8.setText('8')

        self.b9 = QtWidgets.QPushButton(self)
        self.b9.setGeometry(QtCore.QRect(210, 210, 90, 90))
        self.b9.setFont(font)
        self.b9.setText('9')

        self.texto = QtWidgets.QLabel(self)
        self.texto.setText('probando ')
        self.texto.move(10,325)

        self.b1.clicked.connect(self.cambiar_texto)

    def cambiar_texto(self):
        #posicion = int(input("posicion: "))
        self.b1.setText('X')




def ventana():
    
    app = QApplication([])
    win = MiVentana()
    
    win.show()
    

    app.exec()
    

ventana()
