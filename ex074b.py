from random import randint
numeros = (randint(0,10), randint(0,10), randint(0,10),
           randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end='')
for n in range(len(numeros)):
    print(f'{numeros[n]} ', end = '')
print()
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
print(f'Em ordem crescente fica: {sorted(numeros)}')