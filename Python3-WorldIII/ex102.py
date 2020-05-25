def fatorial(num, show=False):
    """
    ->Calcula o fatorial de um número.
    :param num: o fatorial a ser calculado
    :param show: (Opcional) mostra ou não a conta
    :return: o processo de calculo de 'c'.
    """
    print('-=' * 10)
    c = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        c *= i
    return c


# programa principal
help(fatorial)
numero = int(input('Digite um numero: '))
print(fatorial(numero, show=True))
