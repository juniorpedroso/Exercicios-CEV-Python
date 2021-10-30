# Exercício 103 do Curso em Vídeo - Aula 21
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.
def ficha(jogador='<desconhecido>', gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    qtd_gols = gols
    if qtd_gols.isalpha() or qtd_gols == '':
        qtd_gols = 0
    print(f'O jogador {jogador} fez {qtd_gols} gol(s) no campeonato.')


# Programa principal
print('-' * 40)
nome = str(input('Nome do jogador: '))
num = input('Número de gols: ')
ficha(nome, num)
