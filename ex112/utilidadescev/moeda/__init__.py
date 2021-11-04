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
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, aum=0, dim=0):
    print('-' * 28)
    print(f'{"RESUMO DO VALOR":^28}')
    #print('RESUMO DO VALOR'.center(30))
    print('-' * 28)
    print(f'Preço analisado:  {moeda(preco):>10}')
    print(f'Dobro do preço:   {dobro(preco):>10}')
    print(f'Metade do preço:  {metade(preco):>10}')
    if aum > 0:
        print(f'{aum:>2}% de aumento:   {aumentar(preco, aum):>10}')
    if dim > 0:
        print(f'{dim:>2}% de redução:   {diminuir(preco, dim):>10}')
    print('-' * 28)
