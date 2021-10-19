completa = list()
pares = list()
impares = list()
while True:
    completa.append(int(input('Digite um número: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 30)
for cont, v in enumerate(completa):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista completa é {completa}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
