n = soma = cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
if cont == 1:
    print('Você informou apenas um número par, o número {}'.format(soma))
elif cont > 1:
    print('A soma dos {} números pares é {}'.format(cont, soma))
else:
    print('Você não informou nenhum número par')
