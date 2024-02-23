from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

class MiVentana(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('TATETI')
        self.resize(310, 400)
        self.lista_botones = []
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
        self.texto.setText('')
        self.texto.move(10,325)

        self.b1.clicked.connect(self.cambiar_texto)
        self.b2.clicked.connect(self.cambiar_texto)
        self.b3.clicked.connect(self.cambiar_texto)
        self.b4.clicked.connect(self.cambiar_texto)
        self.b5.clicked.connect(self.cambiar_texto)
        self.b6.clicked.connect(self.cambiar_texto)
        self.b7.clicked.connect(self.cambiar_texto)
        self.b8.clicked.connect(self.cambiar_texto)
        self.b9.clicked.connect(self.cambiar_texto)

        self.lista_botones.extend([self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9,])
        self.jugador = 'X'

    
    def cambiar_texto(self):
        boton = self.sender()
        if self.jugador == 'X':
            boton.setText('X')
            self.jugador = 'O'
        else:
            boton.setText('O')
            self.jugador = 'X'
        winner, player = chequeo_ganador(self.ver_posiciones())
        if winner:
            self.texto.setText(f'Ganador: {player}')
        

    def ver_posiciones(self):
        posiciones = []
        for boton in self.lista_botones:
            posiciones.append(boton.text())
        return posiciones

def chequeo_ganador(positions: list):
    # check vertical
    for i in range(0, 3):
        if positions[i] == positions[i + 3] == positions[i + 6]:
            if positions[i] == 'X' or positions[i] == 'O':
                win = positions[i]
                return True, win
    # check horizontal
    for i in range(0, 9, 3):
        if positions[i] == positions[i + 1] == positions[i + 2]:
            if positions[i] == 'X' or positions[i] == 'O':
                win = positions[i]
                return True, win
    # check diagonal
    if positions[0] == positions[4] == positions[8]\
    or positions[2] == positions[4] == positions[6]:
        if positions[4] == 'X' or positions[4] == 'O':
            win = positions[4]
            return True, win
    win = '0'
    return False, win

'''
def jugador():
    for i in range(0, 9):
        if i % 2 == 0:
            jugador = 'X'
        else:
            jugador = 'O'
        return jugador

        winner, win = chequeo_ganador(positions)
        if winner:
            print(f'The winner is: {win}')
            break

'''


def ventana():
    
    app = QApplication([])
    win = MiVentana()
    
    win.show()

    app.exec()
    

ventana()
