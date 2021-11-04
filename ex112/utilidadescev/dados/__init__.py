def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(f'{msg}')).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(valor)


def leiaInt(msg):
    while True:
        num = str(input(f'{msg}')).strip()
        if not num.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return num
