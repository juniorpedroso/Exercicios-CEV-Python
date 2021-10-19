dados = list()
pessoas = list()
pesomax = pesomin = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        pesomax = pesomin = dados[1]
    else:
        if pesomax < dados[1]:
            pesomax = dados[1]
        if pesomin > dados[1]:
            pesomin = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 40)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {pesomax}Kg. Peso de ', end='')
for pessoamax in pessoas:
    if pessoamax[1] == pesomax:
        print(pessoamax[0], end=' ')
print(f'\nO menor peso foi {pesomin}Kg. Peso de ', end='')
for pessoamin in pessoas:
    if pessoamin[1] == pesomin:
        print(pessoamin[0], end=' ')


