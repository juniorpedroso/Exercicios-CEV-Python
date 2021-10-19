from time import sleep
from random import randint
jogos = []
dados = []
num = 0
print('-=' * 20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-=' * 20)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
for cont_jogos in range(0, qtd):    # um loop com a quantidade escolhida pelo usuário
    for cont_num in range(0, 6):    # um loop de 6 para os números
        while True:
            num = randint(1, 60)    # Busca um número aleatório
            if cont_num == 0:       # Verifica se é o primeiro número
                break
            else:
                if num in dados:    # Verifica se já existe este número
                    continue        # Se sim, continua no loop
                else:
                    break           # Se não, sai do loop
        dados.append(num)           # adiciona o número na lista temporária
        if cont_num == 5:
            dados.sort()            # Coloca os números em ordem
            jogos.append(dados[:])  # Insere os dados na lista principal
            dados.clear()           # Apaga a lista temporária
print('-=' * 4, f'SORTEANDO {qtd} JOGOS', '-=' * 4)
#print(f"<<<<<  SORTEANDO {qtd} JOGOS  >>>>>")
for i in range(0, qtd):
    sleep(1)
    print(f'Jogo {i + 1:>2}: {jogos[i]}')
print('-=' * 20)
