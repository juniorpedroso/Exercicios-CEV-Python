'''n = float(input('Digite um número real: '))
print('A parte inteira deste número é {}'.format(int(n)))
print('A parte decimal deste número é {}'.format(n - int(n)))'''

from math import trunc
n = float(input('Digite um número real: '))
print('A parte inteiro deste número é {}'.format(trunc(n)))
