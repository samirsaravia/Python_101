from ex115.lib.interface import *


def arquivo_existe(nome):
    """
    -> verifica se existe o nome do arquivo
    :param nome: nome do arquivo à verificar
    :return: :var a : Veracidade da existencia
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        print('Arquivo pronto para ser criado!...')
    except Exception as error:
        print(f'Houve um erro "{error.__class__}"')
    else:
        return True


def criar_arquivo(nome):
    """
    -> Cria um arquivo com o seguinte param
    :param nome: nome do arquivo à criar
    """
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as error:
        print(f'Houve um erro na criação do arquivo " {error.__class__} "')
    else:
        print(f'\033[0;32mArquivo {nome} criado com sucesso!\033[m')


def ler_arquivo(nome):
    """
    -> Mostra na tela o conteudo de um arquivo com a seguinte param
    :param nome: nome do arquivo à ler
    """
    try:
        a = open(nome, 'rt')
    except Exception as error:
        print(f'Houve um erro ao ler o arquivo {error.__class__}')
    else:
        titulo('pessoas cadastradas')
        cont = 0
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            cont += 1
            print(f'{cont:<4}{dado[0]:.<30}{dado[1]:<4}anos')
        a.close()


def pessoa(texto):
    """

    :param texto:
    :return:
    """
    while True:
        p = input(texto).strip().upper()
        if p.isdigit() or p == '':
            print('Erro, digite um nome válido por favor.')
        else:
            return p


def cadastrar_pessoa(arquivo, nome_pessoa, idade_pessoa):
    """

    :param arquivo:
    :param nome_pessoa:
    :param idade_pessoa:
    :return:
    """
    try:
        a = open(arquivo, 'at')
    except Exception as erro:
        print('Houve um erro ao abrir o arquivo')
        print(f'{erro.__class__}')
    else:
        try:
            a.write(f'{nome_pessoa};{idade_pessoa}\n')
        except Exception as erro:
            print(f'Houve um erro {erro.__class__}')
        else:
            print(f'Novo registro "{nome_pessoa.capitalize()}" adicionado.')
            a.close()
