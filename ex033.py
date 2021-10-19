num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
#verificando quem é o número maior
maior = num1
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
# verificando quem é o número menor
menor = num1
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
print('O número menor é {} e o número maior é {}'.format(menor, maior))
