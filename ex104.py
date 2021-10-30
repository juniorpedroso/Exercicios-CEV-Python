# Exercício 103 do Curso em Vídeo - Aula 21
# Crie um programa que tenha a função leiaint() do Python,
# só que fazendo a validação para aceitar apenas um valor
# numérico.
# # Ex.: leiaint('Digite um número: )
# Usando o sistema de cores ANSI \033[m
def leiaInt(msg):
    while True:
        num = str(input(f'{msg}')).strip()
        if not num.isnumeric():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return num


# Programa principal
print('-=' * 30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
print()
