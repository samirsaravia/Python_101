from time import sleep


def cor(lb_ffuc=False, lp_fa=False, lp_fb=False, lb_fvm=False, fim_c=False):
    """
    -> Cores (Opcionais)
    :param lb_ffuc: letra branca, fundo fuccia
    :param lp_fa: letra preta, fundo azul
    :param lp_fb: letra preta, fundo branco
    :param lb_fvm: letra branca, fundo vermelho
    :param fim_c: fim da cor
    :return: código das cores escolhidas.
    """
    if lb_ffuc:
        return '\033[1;45m'
    if lp_fa:
        return '\033[1;30;44m'
    if lp_fb:
        return '\033[7;97m'
    if lb_fvm:
        return '\033[1;97;41m'
    if fim_c:
        return '\033[m'


def lin(lugar_linha):
    """
    -> Linha que se adapta a frase
    :param lugar_linha: calcula quantas palavras tem a frase (com +2 espaços adicionados/final)
    """
    print(f'{"~" * (len(lugar_linha) + 2)}')
    
    
def py_help():
    """
    -> Ajuda interativa usando o help()
    :return: resultado da pesquisa ,dentro do help() e usa cores de funções.
    """
    bibl = {'title': '  Sistema de ajuda Py_help', 'acesso': '  Acessando ao comando ', 'fim': '  Até Logo'}
    busca = ' '
    while busca != 'fim':
        sleep(1.6)
        print(f'{cor(fim_c=True)}{cor(lb_ffuc=True)}', end='')
        lin(bibl['title'])
        print(bibl['title'])
        lin(bibl['title'])
        busca = input(f'{cor(fim_c=True)}{"Função ou Biblioteca >>> "}').lower().strip()
        if busca == 'fim':
            sleep(1.3)
            print(cor(lb_fvm=True), end='')
            lin(bibl['fim'])
            print(bibl["fim"])
            lin(bibl['fim'])
            break
        else:
            sleep(2)
            print(cor(lp_fa=True), end='')
            lin(bibl['acesso'] + busca)
            print(f'{bibl["acesso"]}{busca}')
            lin(bibl['acesso'] + busca)
            sleep(3)
            print(f'{cor(fim_c=True)}{cor(lp_fb=True)}', end='')
            help(busca)
            
    return help


# programa principal
py_help()
