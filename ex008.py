a = float(input('Digite um valor em metros: '))
#b = a * 100
#c = a * 1000
#print('Este valor é equivalente a {} Centímetros e a {} Milímetros'.format(b, c))
print(f'A medida de {a:.1f}m corresponde a:')
print(f'{a/1000}km')
print(f'{a/100}hm')
print(f'{a/10}dam')
print(f'{a*10}dm')
print(f'{a*100}cm')
print(f'{a*1000}mm')
