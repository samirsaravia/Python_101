def aumentar(num=0, p=0):
    f = num + (num * p) / 100
    return f


def reducir(num=0, p=0):
    f = num - (num * p) / 100
    return f


def dobro(num=0):
    f = num * 2
    return f


def metade(num=0):
    f = num / 2
    return f


def moeda(num, moeda: str = 'R$'):
    """
    :type num: float
    :type moeda: str
    """
    return f'{moeda}{num:.2f}'.replace('.', ',')
