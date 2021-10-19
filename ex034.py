salario = float(input('Qual é o seu atual salário?: R$'))
if salario > 1250:
    aumento = 10
    novosalario = salario * (1 + 10 / 100)
else:
    aumento = 15
    novosalario = salario * (1 + 15 / 100)
print('O valor do novo salário com um aumento de {}% é R${:.2f}'.format(aumento, novosalario))
