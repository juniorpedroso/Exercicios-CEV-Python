from datetime import date
nascimento = int(input('Olá Atleta! Em que ano você nasceu? '))
idade = date.today().year - nascimento
print('Você tem {} anos, então sua categoria é '.format(idade), end='')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JUNIOR.')
elif idade <= 25:
    print('SENIOR.')
else:
    print('MASTER.')
