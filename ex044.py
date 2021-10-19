valor = float(input('Qual o valor do produto? R$'))
forma_pag = int(input('''Escolha a forma de pagamento:
[ 1 ] Dinheiro / Cheque á vista
[ 2 ] Cartão\n'''))

if forma_pag == 1:
    pagamento = valor - (valor * 10 / 100)
    print('Pagando em dinheiro ou cheque a vista o valor, \ncom 10% de desconto, será R${:.2f}'.format(pagamento))
else:
    vezes = int(input('Escolha em quantas parcelas: '))
    if vezes == 1:
        pagamento = valor - (valor * 5 / 100)
        print('Pagando no cartão em 1 vez, com 5% de desconto, R${:.2f}'.format(pagamento))
    elif vezes == 2:
        pagamento = valor / 2
        print('Pagamento no cartão, sem desconto, em 2 vezes de R${:.2f}'.format(pagamento))
    else:
        pagamento = valor + (valor * 20 / 100)
        print('Pagamento no cartão, com acréscimo de 20%')
        print('Em {} parcelas de R${:.2f}'.format(vezes, (pagamento / vezes)))
        print('Totalizando o valor de R${:.2f}'.format(pagamento))
