# Exercício 92 apresentando na aula 19 do Curso em Vídeo
# Segunda VERSÃO
from datetime import datetime
ano = datetime.now().year  # Como buscar o ano atual usando a função now()
nasctemp = ''
print('-=' * 22)
print(f'{"-<" * 4}{"  CADASTRO DE FUNCIONÁRIOS  "}{">-" * 4}')
print('-=' * 22)
funcionarios = []
dados = dict()
while True:
    dados['nome'] = str(input('Nome: '))
    dados['nascimento'] = int(input('Ano de nascimento: '))
    dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if dados['ctps'] != 0:
        dados['ano_contrato'] = int(input('Ano de contratação: '))
        dados['salario'] = float(input('Salário: R$ '))
    funcionarios.append(dados.copy())
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('=' * 74)
print('Cód |Nome             |Nasc |Idade |CTPS   | Ano Cont | Salário  | Aposent')
print('=' * 74)
for f in range(0, len(funcionarios)):
    print(f'{f:>4}|{funcionarios[f]["nome"]:<17}|{funcionarios[f]["nascimento"]:<5}|', end='')
    print(f'{ano - funcionarios[f]["nascimento"]:<6}|{funcionarios[f]["ctps"]:<7}|', end='')
    if funcionarios[f]['ctps'] != 0:
        print(f'{funcionarios[f]["ano_contrato"]:^10}|{funcionarios[f]["salario"]:>10.2f}|', end='')
        print(f'{funcionarios[f]["ano_contrato"] + 30 - funcionarios[f]["nascimento"]:^8}')
    else:
        print()
print('=' * 74)
