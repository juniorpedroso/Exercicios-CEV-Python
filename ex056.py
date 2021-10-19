nomevelho = ''
idadevelho = 0
qtdmulher = 0
totalidade = 0
for cont in range(1,5):
    print('----- {}ª PESSOA -----'.format(cont))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').upper()
    totalidade += idade
    if sexo == 'M':
        if idade > idadevelho:
            idadevelho = idade
            nomevelho = nome
    else:
        if idade < 20:
            qtdmulher += 1
mediaidade = totalidade / 4
print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho é {} que tem {} anos'.format(nomevelho, idadevelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(qtdmulher))
