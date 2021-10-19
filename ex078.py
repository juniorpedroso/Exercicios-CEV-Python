valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
print('-=' * 20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == max(valores):
        print(f'{pos}...', end=' ')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições: ', end='')
for pos, v in enumerate(valores):
    if v == min(valores):
        print(f'{pos}...', end=' ')
