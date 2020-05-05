from time import sleep
lista_numeros: list = list()
cont = 0
while True:
    numero = input('Digite um numero: ')
    if numero.isdigit():
        numero = int(numero)
        if numero not in lista_numeros:
            lista_numeros.append(numero)
            cont += 1
        else:
            print('Número já digitado')
        flag = ' '
        while flag not in 'SsNn':
            flag = str(input('Deseja continuar [S/N]: '))[0]
        if flag in 'Nn':
            break
    else:
        print('Digito não reconhecido! ')
sleep(2)
print('---' * 15)
print(f'Lista em ordem decrescente : {sorted(lista_numeros, reverse=True)}')
if 5 in lista_numeros:
    print(f'O numero \'5\' foi digitado,')
else:
    print('o numero \'5\' não foi digitado.')
print(f'Foram digitados {cont} números.')
