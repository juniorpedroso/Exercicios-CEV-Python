# Módulo Interface do ex115

def leiaInt(msg):
    """[Esta função solicita um valor e verifica se é um número inteiro]

    Args:
        msg ([string]): [Recebe mensagem a ser mostrada]

    Returns:
        [int]: [Se o número for inteiro ele será retornado, 
                 caso contrário uma mensagem será exibida]
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse  número.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao