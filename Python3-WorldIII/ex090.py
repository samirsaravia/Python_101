aluno: dict = dict()
aluno['nome'] = str(input('Nome: ')).upper()
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação'] = f'\033[1;32m{"aprovado".upper()}\033[m'
else:
    aluno['situação'] = f'\033[1;31m{"reprovado".upper()}\033[m'
print('---' * 10)
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situação"]}')
