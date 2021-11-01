def aumentar(val, porc):
    """[Esta função aumenta o valor com a referida porcentagem]

    Args:
        val ([float]): [Valor que será acrescido]
        porc ([float]): [Porcentagem que será incrementada]
    """
    res = val * (1 + (porc / 100))
    return res


def diminuir(val, porc):
    """[Esta função diminui o valor com a referida porcentagem]

    Args:
        val ([float]): [Valor que será diminuido]
        porc ([float]): [Porcentagem que será reduzida]
    """
    res = val * (1 - (porc / 100))
    return res


def dobro(val):
    """[Esta função dobra o valor passado]

    Args:
        val ([float]): [Valor que será dobrado]
    """
    res = val * 2
    return res


def metade(val):
    """[Esta função calcula a metade do valor passado]

    Args:
        val ([float]): [Valor que será reduzido pela metade]
    """
    res = val / 2
    return res


def moeda(preco=0, moeda='R$'):
    #    res = str(f'R$ {preco:.2f}')
    #    res = list(res)
    #    res[-3] = ','
    #    res = ''.join(res)
    #    return res
    return f'{moeda} {preco:.2f}'.replace('.', ',')
