# Exercício 93 do Curso em Vídeo de Python - Versão B
jogador = dict()
gol = []
partidas = 0
print('-=' * 30)
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(partidas):
    gol.append(int(input(f'    Quantos gols na partida {p + 1}? ')))
jogador['gols'] = gol.copy()
jogador['total'] = sum(jogador['gols'])
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print()