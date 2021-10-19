print('{:=^40}'.format(' LOJAS PEDROSO '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    pagamento = preço - (preço * 10 / 100)
elif opcao == 2:
    pagamento = preço - (preço * 5 / 100)
elif opcao == 3:
    parcela = preço / 2
    pagamento = preço
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    qtdparcelas = int(input('Quantas parcelas? '))
    pagamento = preço + (preço * 20 / 100)
    parcelas = pagamento / qtdparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(qtdparcelas, parcelas))
else:
    pagamento = 0
    print('Opçao inválida!!!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, pagamento))
