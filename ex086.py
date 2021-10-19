matriz = [[], [], []]
linha = coluna = 0
while True:
    matriz[linha].append(int(input(f'Digite um valor para [{linha}], [{coluna}]: ')))
    coluna += 1
    if coluna == 3:
        if linha == 2:
            break
        else:
            linha += 1
            coluna = 0
print('-=' * 30)
for i in matriz:
    print(f'[{i[0]:^5}] [{i[1]:^5}] [{i[2]:^5}]')
