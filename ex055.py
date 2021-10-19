maior = 0
menor = 0
for cont in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(cont)))
    if peso > maior:
        maior = peso
    if peso < menor or cont == 1:
        menor = peso
print('O peso digitado maior foi {:.1f}Kg e o menor foi {:.1f}Kg'.format(maior, menor))