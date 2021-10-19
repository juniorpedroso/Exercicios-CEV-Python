# Exercício 92 apresentando na aula 19 do Curso em Vídeo
from datetime import datetime
ano = datetime.now().year
nasctemp = ''
print('-=' * 22)
print(f'{"-<" * 4}{"  CADASTRO DE FUNCIONÁRIOS  "}{">-" * 4}')
print('-=' * 22)
funcionarios = []
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['ano_contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
print(dados)
for k, v in dados.items():
    if k == 'nascimento':
        print(f'idade tem o valor de {ano - v}')
        nasctemp = v
    else:
        print(f'{k} tem o valor de {v}')
    if k == 'ano_contrato':
        print(f'Ele se aposentará com {v + 30 - nasctemp}')
