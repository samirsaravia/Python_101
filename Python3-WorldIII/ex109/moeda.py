def aumento(num=0, p=0, form=False):
    """
    -> Calcula uma porcentagem e soma
    :param num: preço
    :param p: porcentagem à calcular
    :param form: (opcional) formatação (.2float e troca de ponto por virgula)
    :return: :var f : que é o resultado do calculo de porcentagem
    """
    f = num + (num * p // 100)
    return f if form is False else moeda(f)


def reduz(num=0, p=0, form=False):
    """
    -> Calcula a porcentagem e reduz do valor ou preço
    :param num: preço (padrão=0)
    :param p: porcentagem(%) (padrão = 0)
    :param form: (opcional) formatação (.2Float trocando o ponto '.' por 'virgula')
    :return:
    """
    f = num - (num * p // 100)
    return f if form is False else moeda(f)


def dobro(num=0, form=False):
    """
    -> Adiciona o dobro ao valor ou preço
    :param num: preço ou valor(padrão = 0)
    :param form: (opcional) formatação (.2Float e troca '.' por ','virgula)
    :return: :var f : dobro do preço ou valor.
    """
    f = num * 2
    return f if not form else moeda(f)


def metade(num=0, form=False):
    """
    -> Reduz a metade(/2) o preço ou valor
    :param num: preço ou valor(padrão=0)
    :param form: (opcional) formatação(.2Float e troca '.', ',')
    :return: :var f: produto da substraçÃO(-50%)
    """
    f = num // 2
    return f if not form else moeda(f)


def moeda(num=0, moed='R$'):
    return f'{moed}{num:.2f}'.replace('.', ',')
