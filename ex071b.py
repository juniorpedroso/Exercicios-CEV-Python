print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
saque = int(input('Que valor você quer sacar? R$'))
total = saque
nota = 50
totalnota =0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota:.0f} cédulas de R${nota:.2f}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnota = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')