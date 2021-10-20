# Exercício 95 do Curso em Vídeo de Python - Uma atualização do exercício 93
jogador = dict()
gol = []
time = []
partidas = 0
while True:
    print('--' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(partidas):
        gol.append(int(input(f'    Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = gol.copy()
    jogador['total'] = sum(jogador['gols'])
    gol.clear()
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break
print('-=' * 30)
print(f'Cod  {"nome":<20} {"gols":<15} total')
print('--' * 30)
for i in range(0, len(time)):
    print(
        f'{i:>3}  {time[i]["nome"]:<20} {str(time[i]["gols"]):<15} {time[i]["total"]}')
print('--' * 30)
while True:
    escolhido = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if escolhido == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {time[escolhido]["nome"]}:')
    for i in range(0, len(time[escolhido]['gols'])):
        print(f'   No jogo {i + 1} fez {time[escolhido]["gols"][i]} gols')
    print('-=' * 30)
print('<< ENCERRANDO ... >>')
