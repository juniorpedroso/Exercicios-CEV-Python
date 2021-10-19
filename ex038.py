print('Vamos comparar dois números')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número, que é {}, é maior que o segundo, que é {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número, que é {}, é maior que o primeiro, que é {}'.format(n2, n1))
else:
    print('Os dois números são iguais')
