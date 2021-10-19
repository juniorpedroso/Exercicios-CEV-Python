from random import randint
computador = randint(1,3)
print('Vamos jogar Jokenpô?')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
usuário = int(input('Qual é a sua jogada? '))
opções = ['PEDRA', 'PAPEL', 'TESOURA']
computador = opções[computador]
usuário = opções[usuário]
print('Eu escolhi {} e você escolheu {}'.format(computador, usuário))
if computador == usuário:
    print('EMPATE!!')
elif computador == 'PEDRA':
    if usuário == 'PAPEL':
        print('Parabéns! Você ganhou, PAPEL embrulha a PEDRA.')
    elif usuário == 'TESOURA':
        print('Ganhei! PEDRA quebra a TESOURA.')
elif computador == 'PAPEL':
    if usuário == 'PEDRA':
        print('Ganhei! PAPEL embrula a PEDRA.')
    elif usuário == 'TESOURA':
        print('Parabéns! Você ganhou, TESOURA corta PAPEL.')
elif computador == 'TESOURA':
    if usuário == 'PEDRA':
        print('Parabéns! Você ganhou, PEDRA quebra a TESOURA')
    if usuário == 'PAPEL':
        print('Ganhei! TESOURA corta PAPEL')
