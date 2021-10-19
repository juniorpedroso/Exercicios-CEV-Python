n = int(input('Digite a quantidade de elementos de Fibonacci: '))
cont = 1
elemento_anterior = 0
elemento = 0
elemento_novo = 0
while cont <= n:
    print(elemento, end=' -> ')
    if elemento == 0:
        elemento_novo = 1
    else:
        elemento_novo = elemento + elemento_anterior
    elemento_anterior = elemento
    elemento = elemento_novo
    cont += 1
print('Acabou')
