# Exercício 106 do Curso em Vídeo - aula 21
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# Obs. Use cores
c = ('\033[m',          # 0 - Sem cores
     '\033[0;97;41m',   # 1 - vermelho
     '\033[0;97;42m',   # 2 - verde
     '\033[0;97;43m',   # 3 - amarelo
     '\033[0;97;44m',   # 4 - azul
     '\033[0;97;46m',   # 5 - roxo
     '\033[0;30;107'    # 6 - branco
     )


def menu(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')


def minhaAjuda(com):
    menu(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


# Programa principal
ajuda = ''
while True:
    menu('SISTEMA DE AJUDA PyHELP', 2)
    ajuda = str(input('Função ou biblioteca > '))
    if ajuda.upper() == 'FIM':
        break
    else:
        minhaAjuda(ajuda)
menu('ATÉ LOGO!', 1)
