from random import randint
num1 = randint(0,10)
num2 = randint(0,10)
num3 = randint(0,10)
num4 = randint(0,10)
num5 = randint(0,10)
numeros = [num1, num2, num3, num4, num5]
print(f'Os números escolhidos foram: {numeros}')
maior = menor = 0
for i in range(len(numeros)):
    if i == 1:
        maior = menor = numeros[i]
    else:
        if numeros[i] < menor:
            menor = numeros[i]
        if numeros[i] > maior:
            maior = numeros[i]
print(f'O menor valor é {menor} e o maior valor é {maior}')