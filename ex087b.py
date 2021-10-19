matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma3col = maior2linha = 0
for l in range(0, 3): # Aqui foi criado um laço para inserir os valores
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}] [{c}]: ')) # Aqui recebe os valores
print('-=' * 30)
for l in range(0, 3): # Início de um laço para imprimir os valores e efetuar os cálculos
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if c == 2:
            print()
        if matriz[l][c] % 2 == 0:  # Pesquisa se é par
            pares += matriz[l][c]
        if c == 2:
            soma3col += matriz[l][c]  # Soma os valores da 3ª coluna
        if l == 1:
            if maior2linha < matriz[l][c]: # Analisa qual é o maior valor da 2ª linha
                maior2linha = matriz[l][c]
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da 3ª coluna é {soma3col}.')
print(f'O maior valor da 2ª linha é {maior2linha}.')
