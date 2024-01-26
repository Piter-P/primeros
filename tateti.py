import random
import time

positions = []

# iniciamos las 9 posiciones vacias
for i in range(0, 9):
    positions.append(' ')

# cual posicion quiere poner X
def player_x(positions):
    positions[int(input('donde: ')) - 1] = 'X'
    # return positions


def computer_player(positions):
    selection = random.randint(0, 8)
    if positions[selection] == ' ':
        positions[selection] = 'O'
        #return positions
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

def win_game(positions):
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
    # check diagonals
    if positions[0] == positions[4] == positions[8]\
    or positions[2] == positions[4] == positions[6]:
        if positions[4] == 'X' or positions[4] == 'O':
            win = positions[4]
            return True, win
    win = '0'
    return False, win


for i in range(0, 9):
    if i % 2 == 0:
        player_x(positions)
    else:
        print('computer choice: ')
        time.sleep(1)
        computer_player(positions)
    print_game()
    winner, win = win_game(positions)
    if winner:
        print(f'the winner is:', win)
        break