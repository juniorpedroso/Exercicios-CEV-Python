print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = int(input('Informe a medida da reta 1: '))
reta2 = int(input('Informe a medida da reta 2: '))
reta3 = int(input('Informe a medida da reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar um triângulo')
