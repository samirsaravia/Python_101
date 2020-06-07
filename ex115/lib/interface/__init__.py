def lin(tam=42):
    print('-' * tam)


def leia_int(menssage):
    """
    -> Lê um número inteiro
    :param menssage: chamada (descrição)
    :return: :var numero: número inteiro após ser aprovado por tratamento de erro
    """
    while True:
        numero = input(menssage)
        try:
            numero = int(numero)
        except (ValueError, TypeError):
            print('\033[1;31mHouve um error! Por favor digite um número válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[0;31mO usuario preferiu não informar\033[m')
        except Exception as error:
            print(f'O erro é {error.__class__}')
        else:
            return numero


def titulo(texto=''):
    lin()
    print(texto.center(42).upper())
    lin()


def menu(lista):
    titulo('Sistema principal')
    c = 0
    for item in lista:
        c += 1
        print(f'\033[0;33m{c}\033[m-\033[1;94m{item}\033[m')
    lin()
    opc = leia_int('\033[0;33mSua opção:\033[m ')
    return opc
