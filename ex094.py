# Exercício 94 do Curso em Vídeo de Python, Aula 19
dados = dict()
pessoas = list()
print('-=' * 30)
tot_idade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')    
    dados['idade'] = int(input('Idade: '))
    tot_idade += dados['idade']     # Aqui eu vou acumulando os valores de idade na variável     
    pessoas.append(dados.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('-=' * 30)
media = (tot_idade / len(pessoas))
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é {media:.1f}')
print('- As mulheres cadastradas foram ', end='')
for i in range(len(pessoas)):
    if pessoas[i]['sexo'] in 'fF':
        if i > 0: print(', ', end='')
        print(pessoas[i]['nome'], end='')
print()
print('Lista das pessoas que estão com idade acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
print('<< ENCERRADO >>')
'''for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        print(f'Nome = {pessoas[i]["nome"]}, sexo = {pessoas[i]["sexo"]}, idade = {pessoas[i]["idade"]}')'''
