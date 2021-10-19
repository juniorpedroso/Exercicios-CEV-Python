from datetime import date
ano = date.today().year
maior = 0
menor = 0
idade = 0
for c in range (1,8):
    nascimento = int(input('Digite a data de nascimento da {}ª pessoa: '.format(c)))
    idade = ano - nascimento
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('No total foram {} maiores e {} menores'.format(maior, menor))
