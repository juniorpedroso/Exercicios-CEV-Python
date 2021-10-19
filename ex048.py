selec = 0
soma = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        selec += 1
        soma += cont
print('A soma de todos os {} números selecionados é {}'.format(selec, soma))
