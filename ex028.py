from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "pensar" em um número
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ....')
print('-=' * 30)
jogador = int(input('Em que número pensei? ')) # O jogador tenta adivinhar
print('Processando......')
sleep(2)
if jogador == computador: # Testa se o jogador acertou
    print('Você acertou. Parabéns!')
else:
    print('Você errou! Eu escolhi {} e não {}'.format(computador, jogador))
