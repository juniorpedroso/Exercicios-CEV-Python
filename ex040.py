nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('\nSua média foi {:.1f}'.format(media), end = ' ')
if media < 5:
    print('\033[1;30;41m REPROVADO!!\033[m')
elif 5 <= media < 7:
    print('\033[1;30;43m RECUPERAÇÃO!!\033[m')
elif media >= 7:
    print('\033[1;97;42m APROVADO!!\033[m')
