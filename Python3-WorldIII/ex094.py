dados_pessoa: dict = dict()
lista_pessoas: list = list()
media: list = list()
mulheres: list = list()
while True:
    dados_pessoa['nome'] = str(input('Nome: ').strip().upper())
    dados_pessoa['idade'] = int(input('Idade: '))
    media.append(dados_pessoa['idade'])
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo[M/F]: ').strip())[0]
        if sexo in 'MmFf':
            dados_pessoa['sexo'] = sexo.upper()
        if sexo in 'Ff':
            mulheres.append(dados_pessoa['nome'])
    lista_pessoas.append(dados_pessoa.copy())
    dados_pessoa.clear()
    flag = ' '
    while flag not in 'SsNn':
        flag = str(input('Deseja continuar: ').strip())[0]
    print('--' * 15)
    if flag in 'Nn':
        break
print(f'    -Foram cadastradas {len(lista_pessoas)} pessoas')
print(f'    -A media de idade é de {sum(media) / len(lista_pessoas):.2f} anos.')
print(f'    -As mulheres cadastradas foram: ', end=' ')
# cm = cada mulher
for cm in mulheres:
    print(f'[{cm}]', end=' ')
print()
print('Lista de pessoas acima da média: ')
print('--' * 16)
# cp =  cada pessoa
for cp in lista_pessoas:
    if cp['idade'] > sum(media) / len(lista_pessoas):
        print(f'{cp["nome"]} com {cp["idade"]} anos,  sexo = {cp["sexo"]}')
print('--' * 15)
print('<< encerrado >>')
