from datetime import datetime
from time import sleep
dados_pessoais: dict = dict()
ano_atual = datetime.now().year
dados_pessoais['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados_pessoais['idade'] = ano_atual - ano_nascimento
ctps = int(input('Carteira de trabalho (0 se não tem): '))
if ctps != 0:
    dados_pessoais['ctps'] = ctps
    dados_pessoais['contratação'] = int(input('Ano de contratação: '))
    dados_pessoais['salario'] = float(input('Salario R$: '))
    dados_pessoais['aposentadoria'] = dados_pessoais['contratação'] + 35 - ano_nascimento
    print('--' * 15)
    sleep(2)
    for k, v in dados_pessoais.items():
        print(f'{k}: {v}')
else:
    print('--' * 15)
    sleep(2)
    for k, v in dados_pessoais.items():
        print(f'{k} : {v}')
