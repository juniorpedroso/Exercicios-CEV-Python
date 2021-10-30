# Exercício 105 do Curso em Vídeo - Aula 21
# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função
def notas(*n, sit=False):
    """ 
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
     """
    dicionario = dict()
    total = maior = menor = media = soma = cont = 0
    situacao = ''
    total = len(n)

    for num in n:
        soma += num
        if cont == 0:
            menor = num
            maior = num
        else:
            if num < menor:
                menor = num
            if num > maior:
                maior = num
        cont += 1

    media = soma / total
    if media > 7:
        situacao = 'BOA'
    elif 6 < media < 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'RUIM'
    dicionario['total'] = total
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit:
        dicionario['situacao'] = situacao

    return dicionario


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
# help(notas)
