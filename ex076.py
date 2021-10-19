listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print('{:^40}'.format(' LISTAGEM DE PREÇOS '))
print('-' * 40)
cont = 0
while True:
    print('{:.<30}'.format(listagem[cont]), end='R$')
    cont += 1
    print('{:>7.2f}'.format(listagem[cont]))
    cont += 1
    if cont >= len(listagem):
        break
print('-' * 40)
