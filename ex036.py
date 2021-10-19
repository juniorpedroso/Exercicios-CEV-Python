print('+$'* 13)
print('\033[1;31m+ Analisador de crédito +\033[m')
print('+$'* 13)
valor_casa = float(input('\nQual o valor da casa que você quer comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
meses = anos * 12
parcela = valor_casa / meses
if parcela > (salario * 30 / 100):
    print('\nSeu financiamento foi NEGADO!\nO valor da parcela seria R${:.2f}\nEste valor supera 30% do seu salário'.format(parcela))
else:
    print('\nSeu financioamento foi APROVADO!\nO valor da parcela será R${:.2f}'.format(parcela))

