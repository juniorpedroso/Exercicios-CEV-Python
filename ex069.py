# Quantas pessoas com mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos
maiores = homens = mulheresjovens = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheresjovens += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresjovens} mulheres com menos de 20 anos')
