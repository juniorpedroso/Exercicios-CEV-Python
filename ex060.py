n = int(input('Digite um número para calcular seu fatorial: '))
print('{}! ='.format(n), end=' ')
resultado = cont = n
while cont > 1:
    print('{} X'.format(cont), end=' ')
    resultado = resultado * (cont - 1)
    cont -= 1
print('1 = {}'.format(resultado))
