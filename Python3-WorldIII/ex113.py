def leia_int(msg):
    # sem tratamento de erro
    """
    -> Func que remplaza o int() e valida o mesmo.
    :param msg: input (descrição que mostra na tela)
    :return: o valor em int() do usuario.
    """
    while True:
        numero = input(msg)
        if numero.isdigit():
            valor = int(numero)
            break
        else:
            print(f'Erro!')
    return valor


def leia_float(num=''):
    # com tratamento de erro.
    """
    ->Func que imita o float() e valida o mesmo, com tratamento de erro.
    :param num: recebe um texto para 'input'
    :return: :var f número válido
    """
    while True:
        f = str(input(num).replace(',', '.').strip())
        try:
            f = float(f)
        except ValueError:
            print('Erro! Escrita não aceita')
        except KeyboardInterrupt:
            print('O usuario não informo esse valor.')
            return 0
        else:
            return f


i = leia_int('Digite um número inteiro: ')
r = leia_float('Digite um número real: ')
print(f'Você digitou um inteiro{i} e um real {r}')
