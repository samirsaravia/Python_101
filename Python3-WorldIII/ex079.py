from time import sleep
from datetime import datetime
lista_valores: list = list()
while True:
    valor = input('Digite um número: ')
    if valor.isdigit():
        valor = int(valor)
        if valor not in lista_valores:
            lista_valores.append(valor)
        else:
            print('Esse valor já foi adicionado.')
            sleep(2)
        question = ' '
        while question not in 'SsNn':
            question = str(input('Deseja continuar[S/N]: '))[0]
        if question in 'Nn':
            break
    else:
        print('Não reconhecido')
print('---' * 15)
print(f'Valores digitados as {datetime.now().hour}:{datetime.now().minute}, os valores: {lista_valores}')
print(f'Valores ordenados (crescente): {sorted(lista_valores)}')
