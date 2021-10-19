cont = media = maior = menor = soma = 0
continua = True
opcao = ' '
while continua:
    n = int(input('Digite um número: '))
    opcao = ' '
    cont += 1
    if maior < n:
        maior = n
    if cont == 1:
        menor = n
    else:
        if menor > n:
            menor = n
    soma += n
    media = soma / cont
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        continua = opcao == 'S'
print('Você digitou {} números e a média foi {:.1f}'.format(cont, media))
print('O número maior é {} e o menor é {}'.format(maior, menor))
print('Fim')