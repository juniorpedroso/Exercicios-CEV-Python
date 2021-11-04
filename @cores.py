def cor(text=0, back=0):
    texto = fundo = 0
    corTotal = ''
    coresText = {'preto': 30,
                 'vermelho': 31,
                 'verde': 32,
                 'amarelo': 33,
                 'azul': 34,
                 'magenta': 35,
                 'ciano': 36,
                 'cinza': 37,
                 'branco': 97, }

    coresBack = {'preto': 40,
                 'vermelho': 41,
                 'verde': 42,
                 'amarelo': 43,
                 'azul': 44,
                 'magenta': 45,
                 'ciano': 46,
                 'cinza': 47,
                 'branco': 107, }

    if text != 0:
        texto = coresText[text]
    if back != 0:
        fundo = coresBack[back]
    if back == 0:
        corTotal = f'\033[{texto}m'
    return [corTotal]
