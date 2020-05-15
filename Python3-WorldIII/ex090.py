aluno: dict = dict()
aluno['nome'] = str(input('Nome: ')).upper()
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação'] = f'\033[1;32m{"aprovado".upper()}\033[m'
else:
    aluno['situação'] = f'\033[1;31m{"reprovado".upper()}\033[m'
print('---' * 10)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')
