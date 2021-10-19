preço = float(input('Qual o preço atual do produto? R$'))
#npreço = preço * 0.95
npreço = preço - (preço * 5 /100)
print('O preço do produto que custava R${:.2f}, na promoção com desconto de 5% será R${:.2f}'.format(preço, npreço))
