from ex115.lib.arquivo import *
from time import sleep

arq = 'dados_cadastrados.txt'
if not arquivo_existe(arq):
    sleep(3)
    criar_arquivo(arq)
sleep(2)
while True:
    resposta = menu(['Ver Pessoas cadastradas', 'Cadastrar Pessoa', 'Sair'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        titulo('Novo cadastro')
        nome = pessoa('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar_pessoa(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo...')
        sleep(1.5)
        break
    else:
        print('   \033[0;31mErro! Por favor digite uma opçao Válida\033[m')
    sleep(1.5)
