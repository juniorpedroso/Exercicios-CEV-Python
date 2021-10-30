from random import randint
from time import sleep


def mostraQuadro():
    # Esta função recebe a lista com os elementos cadastrados na lista elementos
    # e preenche a tela com as alterações.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|{el[0][0]:^7}|{el[0][1]:^7}|{el[0][2]:^7}|')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|{el[1][0]:^7}|{el[1][1]:^7}|{el[1][2]:^7}|')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|{el[2][0]:^7}|{el[2][1]:^7}|{el[2][2]:^7}|')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def listaVazios():
    # A função percorre a lista com os elementos e cria uma lista com os campos vazios;
    # A lista contém tuplas, onde cada tupla contém um par de números indicando determinando uma linha e uma coluna.
    vazio = list()
    pos = list()
    for lin in range(0, 3):
        for col in range(0, 3):
            if str(el[lin][col]) not in 'OX':
                pos = (lin, col)
                vazio.append(pos)
    return vazio


def meuMovimento():
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    mov = escolha = 0
    while True:
        mov = int(input('Digite sua posição: '))
        escolha = indice[mov - 1]
        if escolha in listaVazios():
            el[escolha[0]][escolha[1]] = 'O'
            mostraQuadro()
            break
        else:
            print('Opção já preenchida! Escolha outro número.')


def testaVitoria(sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    if el[0][0] == el[0][1] == el[0][2] or \
       el[1][0] == el[1][1] == el[1][2] or \
       el[2][0] == el[2][1] == el[2][2] or \
       el[0][0] == el[1][1] == el[2][0] or \
       el[0][1] == el[1][1] == el[2][1] or \
       el[0][2] == el[1][2] == el[2][2] or \
       el[0][0] == el[1][1] == el[2][2] or \
       el[0][2] == el[1][1] == el[2][0]:
        print(f'O ganhador foi {sign}')
        ganhador = sign
        return True


def compMovimento():
    # The function draws the computer's move and updates the board.
    print('Agora é minha vez')
    while True:
        myOption = randint(1, 9)
        myOption = indice[myOption - 1]
        if myOption in listaVazios():
            el[myOption[0]][myOption[1]] = 'X'
            sleep(2)
            mostraQuadro()
            break


el = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   # Elementos do tabuleiro
indice = ((0, 0), (0, 1), (0, 2), (1, 0),
          (1, 1), (1, 2), (2, 0), (2, 1), (2, 2))
#            1       2       3       4       5       6       7       8       9
ganhador = ' '

mostraQuadro()
print('O computador fará o primeiro movimento')
sleep(2)
el[1][1] = 'X'
mostraQuadro()
print('Agora é sua vez')
while ganhador == ' ':
    meuMovimento()
    if testaVitoria('Jogador'):
        break
    compMovimento()
    if testaVitoria('Computador'):
        break
print('Foi um ótimo jogo!!!')
