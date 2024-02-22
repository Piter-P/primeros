import random
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from uitateti import Ui_main

positions = []

def posiciones_vacias(positions: list) -> list:
    # iniciamos las 9 posiciones vacias
    for i in range(0, 9):
        positions.append(' ')
    return positions


def jugador_x(positions: list) -> list:
    # cual posicion quiere poner X. Verifica lugar vacio y devuelve las posiciones
    while True:
        try:
            lugar = int(input('Jugador X: '))
            if 1 <= lugar <= 9 and positions[lugar - 1] == ' ': 
                positions[lugar - 1] = 'X'
                return positions
            else:
                print('Posicion incorrecta. Intentelo de nuevo.')
        except:
            print('Error!')
            pass

    '''
    La eleccion de la posicion del jugador es distinta a la de la maquina ya que el usuario puede poner
    cualquier caracter o frase en el input por lo que hay que verificar el paso a int y lugar vacio. 
    En cambio la compu hace random de int dentro de las posiciones y si no esta vacia hace una recursion
    del random
    '''

def computer_player(positions: list) -> list:
    # posicion random de jugador O. verifica lugar vacio y devuelve posiciones.
    selection = random.randint(0, 8)
    if positions[selection] == ' ':
        positions[selection] = 'O'
        return positions
    else:
        computer_player(positions)


def print_game():
    posicion = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if positions[posicion] == ' ':
                print(f' {posicion + 1} ', end=' ')
            else:
                print(f' {positions[posicion]} ', end=' ')
            posicion += 1
        print('')

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

def juego():
    posiciones_vacias(positions)
    for i in range(0, 9):
        if i % 2 == 0:
            jugador_x(positions)
        else:
            print('computer choice: ')
            time.sleep(1)
            computer_player(positions)
        print_game()
        winner, win = chequeo_ganador(positions)
        if winner:
            print(f'The winner is: {win}')
            break




class MiVentana(QMainWindow, Ui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

    


if __name__ == "__main__":
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    juego()
    app.exec()
