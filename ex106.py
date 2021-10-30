# Exercício 106 do Curso em Vídeo - aula 21
# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

# Obs. Use cores
def menu(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))


def minhaAjuda():
    ajuda = ''
    while ajuda != 'FIM':
        print('\033[0;97;42m')  # branco e verde
        menu('SISTEMA DE AJUDA PyHELP')
        print('\033[m')
        ajuda = str(input('Função ou biblioteca > '))
        if ajuda != 'FIM':
            print('\033[0;97;44m')  # branco e azul
            menu(f"Acessando o manual do comando '{ajuda}'")
            print('\033[0;30;107m')  # preto e branco
            help(f'{ajuda}')
            print('\033[m')
    print('\033[0;97;41m')        
    menu('ATE LOGO!')
    print('\033[m')

# Programa principal
minhaAjuda()
