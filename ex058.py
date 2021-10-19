from random import randint
computador = randint(0, 10) # Faz o computador "pensar" em um número
print('Vou pensar em um número entre 0 e 10. Tente adivinhar ....')
jogador = int(input('Em que número pensei? ')) # O jogador tenta adivinhar
cont = 1
while jogador != computador:
    cont += 1
    if jogador > computador:
        jogador = int(input('Menos... Tente mais uma vez: '))
    else:
        jogador = int(input('Mais... Tente mais uma vez: '))
print('Acertou! Você precisou de {} tentativas'.format(cont))
