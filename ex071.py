print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
saque = nota1 = nota10 = nota20 = nota50 = 0
saque = int(input('Que valor você quer sacar? R$'))
if saque // 50 > 0:
    nota50 = saque // 50
    saque = saque - (50 * nota50)
if saque // 20 > 0:
    nota20 = saque // 20
    saque = saque - (20 * nota20)
if saque // 10 > 0:
    nota10 = saque // 10
    saque = saque - (10 * nota10)
nota1 = saque
if nota50 > 0:
    print(f'Total de {nota50:.0f} cédulas de R$50,00')
if nota20 > 0:
    print(f'Total de {nota20:.0f} cédulas de R$20,00')
if nota10 > 0:
    print(f'Total de {nota10:.0f} cédulas de R$10,00')
if nota1 > 0:
    print(f'Total de {nota1:.0f} cédulas de R$1,00')
print('=' * 40)