def aumentar(val=0, porc=0, f=True):
    """[Esta função aumenta o valor com a taxa recebida]

    Args:
        val (int, optional): [Valor recebido a ser acrescido]. Defaults to 0.
        porc (int, optional): [Valor da taxa a ser incrementada]. Defaults to 0.
        f (bool, optional): [Valor será formatado ou não]. Defaults to True.

    Returns:
        [type]: [Valor incrementado ou não, formatado ou não]
    """
    res = val * (1 + (porc / 100))
    return moeda(res) if f else res


def diminuir(val=0, porc=0, f=True):
    """[Esta função diminui o valor com a taxa recebida]

    Args:
        val (int, optional): [Valor recebido a ser diminuido]. Defaults to 0.
        porc (int, optional): [Taxa utilizada na diminuição]. Defaults to 0.
        f (bool, optional): [True - formata o retorno como moeda, Falso não]. Defaults to True.

    Returns:
        [type]: [Valor diminuido ou não, formatado ou não]
    """
    res = val * (1 - (porc / 100))
    return moeda(res) if f else res


def dobro(val=0, f=True):
    """[Esta função calcula o dobro do valor passado]

    Args:
        val (int, optional): [Valor que será dobrado]. Defaults to 0.
        f (bool, optional): [True - formata o retorno como moeda, Falso não]. Defaults to True.

    Returns:
        [type]: [Valor dobrado ou não, formatado ou não]
    """
    res = val * 2
    return moeda(res) if f else res


def metade(val=0, f=True):
    """[Esta função calcula a metade do valor passado]

    Args:
        val ([float]): [Valor que será reduzido pela metade]
    if f:
        return moeda(res)
    else:
        return res
    """
    res = val / 2
    return moeda(res) if f else res


def moeda(preco=0, moeda='R$'):
    """[Esta função formata o preço como moeda, como padrão em R$]

    Args:
        preco (int, optional): [Valor que será formatado]. Defaults to 0.
        moeda (str, optional): [Símbolo da moeda]. Defaults to 'R$'.

    Returns:
        [type]: [Valor formatado]
    """
    return f'{moeda} {preco:.2f}'.replace('.', ',')
