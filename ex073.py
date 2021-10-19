brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
               'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
               'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
               'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print('Os cinco primeiros colocados são:')
for i in range(5):
    print(f'{i+1}º - {brasileirao[i]}')
print(brasileirao[-4:]) # Os últimos quatro colocados
print(sorted(brasileirao)) # Uma lista em ordem alfabética
print(f'O Chapecoense está na {(brasileirao.index("Chapecoense") + 1)}ª posição')
for pos, t in enumerate(brasileirao):
    if pos % 5 == 0:
        print('\n')
    print(t, end=', ')
print('Acabou')