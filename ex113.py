# Exercício 113 do Curso em Video - Aula 23
# TRATAMENTO DE ERROS - EXCEÇÕES
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


def leiaFloat(msg):
    """[Esta função solicita um valor e verifica se é um número real]

    Args:
        msg ([string]): [Recebe mensagem a ser mostrada]

    Returns:
        [float]: [Se o número for real ele será retornado, 
                 caso contrário uma mensagem será exibida]
    """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mUsuário preferiu não digitar esse  número.\033[m')
            return 0
        else:
            return num


# Programa principal
print('-=' * 30)
i = leiaInt('Digite um inteiro: ')
r = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}.')
print()
