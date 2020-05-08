# criar uma lista agrupando dados de pessoas com ajuda de outra lista
# mostrar quem tem o maior e o menor peso
origin: list = list()
support: list = list()
maior = menor = 0
while True:
    support.append(str(input('Nome: ')))
    support.append(int(input('Peso: ')))
    if len(origin) == 0:
        maior = menor = support[1]
    else:
        if support[1] > maior:
            maior = support[1]
        if support[1] < menor:
            menor = support[1]
    origin.append(support[:])
    support.clear()
    flag = ' '
    while flag not in 'SsNn':
        flag = str(input('Deseja continuar[S/N]: '))[0]
    if flag in 'Nn':
        break
print('===' * 15)
print(f'Foram cadastradas {len(origin)} pessoas.')
print()
print(f'O maior peso é: {maior}kg : ', end='')
for dados in origin:
    if maior == dados[1]:
        print(f'[{dados[0]}] ', end=' ')
print()
print(f'O menor peso é de {menor}Kg. :', end='')
for dados in origin:
    if menor == dados[1]:
        print(f'[{dados[0]}] ', end=' ')
print()
