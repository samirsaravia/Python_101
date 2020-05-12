from time import sleep
cadastro: list = []
aluno: list = list()
nota: list = list()
media = list()
while True:
    nome_aluno: str = str(input('Nome:')).upper()
    aluno.append(nome_aluno)
    # qnotas = quantidade de notas
    # qnotas = int(input('Quantas notas serão cadastradas: '))
    for n in range(0, 2):
        nota_aluno = float(input(f'Nota {n + 1}°: '))
        nota.append(nota_aluno)
    m = sum(nota) / 2
    media.append(f'{m:.2f}')
    nota.append(media[:])
    aluno.append(nota[:])
    cadastro.append(aluno[:])
    media.clear(), nota.clear(), aluno.clear()
    flag = ' '
    while flag not in 'NnSs':
        flag: str = input('Deseja continuar[S/N]: ')[0]
    if flag in 'Nn':
        break
print('===' * 15)
print(f'{"N°":<10}', end=' '), print(f'{"Nome":<15}'.upper(), end=' '), print(f'{"Media":<15}'.upper())
cont = 0
for posição, nome in enumerate(cadastro):
    cont += 1
    print(f'{posição:<10} {nome[0]:<15} {nome[1][-1][0]:<15}')
print('===' * 15)
while True:
    dado_aluno = int(input('Mostrar notas de qual aluno[999 interrompe]: '))
    if dado_aluno <= len(cadastro) - 1:
        print(f'Notas de {cadastro[dado_aluno][0]} são: {cadastro[dado_aluno][1][0]} e {cadastro[dado_aluno][1][1]}')
    print('---' * 15)
    if dado_aluno == 999:
        print('Finalizando...')
        sleep(2)
        print('<<<Volte Sempre!!>>>')
        break
