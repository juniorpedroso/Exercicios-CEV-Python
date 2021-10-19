from random import randint
from time import sleep
computador = randint(0,2)
print('Vamos jogar Jokenpô?')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
usuário = int(input('Qual é a sua jogada? '))
opções = ('PEDRA', 'PAPEL', 'TESOURA')
#computador = opções[computador]
#usuário = opções[usuário]
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(opções[computador]))
print('Usuário jogou {}'.format(opções[usuário]))
print('-=' * 11)
if computador == usuário:
    print('EMPATE!!')
elif computador == 0: # 'PEDRA':
    if usuário == 1: # 'PAPEL':
        print('Parabéns! Você ganhou, PAPEL embrulha a PEDRA.')
    elif usuário == 2: # 'TESOURA':
        print('Ganhei! PEDRA quebra a TESOURA.')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #'PAPEL':
    if usuário == 0: # 'PEDRA':
        print('Ganhei! PAPEL embrula a PEDRA.')
    elif usuário == 2: #'TESOURA':
        print('Parabéns! Você ganhou, TESOURA corta PAPEL.')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #'TESOURA':
    if usuário == 0: #'PEDRA':
        print('Parabéns! Você ganhou, PEDRA quebra a TESOURA')
    elif usuário == 1: # 'PAPEL':
        print('Ganhei! TESOURA corta PAPEL')
    else:
        print('JOGADA INVÁLIDA')
