from datetime import datetime


def voto(nasc=0):
    """
    -> Calcula idade e mostra na tela
    :param nasc: nascimento
    :return: sem retorno
    autor: samir
    """
    ano_atual = datetime.now().year
    idade = ano_atual - nasc
    if nasc == 0:
        print('Sem dados')
    else:
        if idade >= 65:
            print(f'Com {idade} anos: Voto opcional')
        else:
            if idade < 18:
                print(f'Com {idade} anos: Não Vota')
            else:
                print(f'Com {idade} anos: Voto obrigatorio')


while True:
    ano = input('Digite o ano de nascimento: ')
    if ano.isdigit():
        ano = int(ano)
        break
    else:
        print('Opçao não valida!')
voto(ano)
