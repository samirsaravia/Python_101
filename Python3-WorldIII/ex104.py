def c(sr=False, sy=False, e=False):
    """
    -> Cores vermelha e amarela
    :param sr: start red(começo vermelho)
    :param sy: start yellow(começo amarelo)
    :param e: end(fim)
    :return: codigo de começo e fim de cor
    """
    if sr:
        return '\033[0;31m'
    if sy:
        return '\033[0;33m'
    if e:
        return '\033[m'


def leia_int(msg):
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
            print(f'{c(sr=True)}Erro!{c(e=True)} {c(sy=True)}{numero}{c(e=True)} {c(sr=True)}Não é valido! {c(e=True)}')
    return valor
    

n = leia_int('Digite um número: ')
print(f'Você digitou o número {n}')
