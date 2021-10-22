def area(l, c):
    m = l * c
    print(f'A área de um terreno {l:.2f} X {c:.2f} é de {m:.2f}m².')


# Programa principal
print('-' * 30)
print(f'{"CONTROLE DE TERRENOS":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m) '))
area(l, c)
