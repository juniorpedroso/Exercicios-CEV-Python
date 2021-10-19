matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma3col = maior2linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: '))
print('-=' * 30)
for i in matriz:
    print(f'[{i[0]:^5}] [{i[1]:^5}] [{i[2]:^5}]')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma3col += matriz[l][c]
        if l == 1:
            if maior2linha < matriz[l][c]:
                maior2linha = matriz[l][c]
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da 3ª coluna é {soma3col}.')
print(f'O maior valor da 2ª linha é {maior2linha}.')
