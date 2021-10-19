from math import sqrt, pow
co = float(input('Informe a medida do Cateto Oposto: '))
ca = float(input('Informe a medida do Cateto Adjacente: '))
hip = sqrt(pow(co,2) + pow(ca, 2))
print('O valor da hipotenusa é {}'.format(hip))
