title = 'Cadastro'.upper()
print('===' * 10)
print(f'\033[7;30m{title:^30}\033[m')
print('===' * 10)
cont = mulher = homem = menor_idade = maior_idade_h = menor_idade_h = menor_idade_m = maior_idade_m = 0
pergunta = ''
while True:
    cont += 1
    idade = int(input('Qual a idade :  '))
    sexo = str(input('Sexo [F/M]:  ')).strip().upper()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Sexo [F/M]:  ')).strip().upper()[0]
    if idade < 18:
        menor_idade += 1
    if sexo in 'Ff' and idade >= 18:
        maior_idade_m += 1
    if sexo in 'Ff' and idade < 18:
        menor_idade_m += 1
    if sexo in 'Ff':
        mulher += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Mm' and idade >= 18:
        maior_idade_h += 1
    if sexo in 'Mn' and idade < 18:
        menor_idade_h += 1
    pergunta = str(input('quere continuar[S/N]:  ')).strip().upper()[0]
    while pergunta not in 'SsNn':
        pergunta = str(input('quere continuar[S/N]:  ')).strip().upper()[0]
    if pergunta in 'Nn':
        break
    print('___' * 10)
stop = 'cadastro Finalizado'.upper()
print(f'\033[7;30m{stop:=^30}\033[m')
print('___' * 10)
print(f'Foram registradas {cont} pessoa/s')
print(f'Há {mulher} mulher/es e {homem} homen/s')
print(f'Há {maior_idade_h} homens acima de 18 anos e {menor_idade_h} menores de idade.')
print(f'Há {maior_idade_m} mulher/es igual ou acima de 18 anos, e {menor_idade_m} menor de idade.')
print(f'Em total há {menor_idade} menores de idade.')
