# Exercício 93 do Curso em Vídeo de Python
jogador = dict()
gol = []
partidas = totalgols = 0
print('-=' * 30)
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(partidas):
    gol.append(int(input(f'    Quantos gols na partida {p + 1}? ')))
    totalgols += gol[p]
jogador['gols'] = gol.copy()
jogador['total'] = totalgols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p in range(len(jogador['gols'])):
    print(f'    => Na partida {p + 1}, fez {jogador["gols"][p]} gols.')
print(f'Foi um total de {totalgols} gols.')
print()
 