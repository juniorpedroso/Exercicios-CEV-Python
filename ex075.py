numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {numeros}')

print(f'O número 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3) > 0:
    print(f'O primeiro número 3 foi digitado na posição {(numeros.index(3)+1)}')
else:
    print('O número 3 não foi digitado em nenhuma posição')
cont = 0
print('Os valores pares digitados foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i,end=' ')
        cont += 1
if cont == 0: print(0)
