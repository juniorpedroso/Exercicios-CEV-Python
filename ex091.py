from random import randint
from time import sleep
jogo = {}
todos = []
print('-=' * 20)
print('Valores sorteados')
print('-=' * 20)
for i in range(0, 4):
    jogo['jogador'] = ('Jogador ' + str(i + 1))
    jogo['dado'] = randint(1, 6)
    todos.append(jogo.copy())
    sleep(1)
    print(f'O {jogo["jogador"]} tirou {jogo["dado"]}')
sleep(1)
print('-=' * 20)
print('Ranking dos jogadores')
print('-=' * 20)
trocado = True
while trocado:
    trocado = False
    for i in range(3):
        if todos[i]['dado'] < todos[i + 1]['dado']:
            trocado = True
            todos[i], todos[i + 1] = todos[i + 1], todos[i]
for e in range(0, 4):
    sleep(1)
    print(f'{e + 1}º lugar:  O {todos[e]["jogador"]} com {todos[e]["dado"]}')  
print('-=' * 20)    
