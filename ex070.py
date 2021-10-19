# A - Qual o total gasto na compra
# B - Quantos produtos custam mais de R$1.000,00
# C - Qual é o nome do produto mais barato
total = qtd1000 = 0
produtobarato = ' '
precoprodutobarato = 0
qtdprodutos = 0
print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    qtdprodutos += 1
    if preco > 1000:
        qtd1000 += 1
    if qtdprodutos == 1:
        precoprodutobarato = preco
        produtobarato = produto
    elif preco < precoprodutobarato:
        precoprodutobarato = preco
        produtobarato = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('--------- FIM DO PROGRAMA --------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtd1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {produtobarato} que custa R${precoprodutobarato}')
