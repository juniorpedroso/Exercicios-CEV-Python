from datetime import date
ano_atual = int(date.today().year)
ano_nasc = int(input('Informe o ano em que nasceu: '))
idade = ano_atual - ano_nasc
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, idade, ano_atual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano_nasc + 18))
elif idade == 18:
    print('Este é o ano em que você deve se alistar, pois está com 18 anos')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Você deveria ter se alistado em {}.'.format(ano_nasc + 18))
