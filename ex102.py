#  Exercídio 102 do Curso em Vídeo - Referente a aula 21
#  Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico
# (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param: n: O número a ser calculado.
    :param: show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''
    cont = n
    fat = 1
    while cont > 0:
        if show:
            if cont == 1:
                print(f'{cont} = ', end='')
            else:
                print(f'{cont} X ', end='')
        fat *= cont
        cont -= 1
    return fat


# Programa principal
print('-' * 50)
print(fatorial(5))
print(fatorial(7, True))
print('-' * 50)
help(fatorial)
