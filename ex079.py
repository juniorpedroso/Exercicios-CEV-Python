valores = []
while True:
    novovalor = int(input('Digite um valor: '))
    if valores.count(novovalor) != 0: # Pesquisa se NOVOVALOR já está dentro da lista
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(novovalor) # Adiciona NOVOVALOR a lista valores
        print('Valor adicionado com sucesso...')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')
