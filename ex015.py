dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
#precodia = dia * 60
#precokm = km * 0.15
#precototal = precodia + precokm
precototal = (dia * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(precototal))
