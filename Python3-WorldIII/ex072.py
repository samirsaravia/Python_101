numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
           , 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

# escolha = int(input('Digite um numero 1-20: '))
# while escolha > 20 or escolha < 0:
#     escolha = int(input('Fora do alcance,digite um numero entre 1-20: '))
# for cont in range(len(numeros)):
#     if escolha == cont:
#         print(f'O número \033[1;33m{numeros[cont]}\033[m foi digitado.')


# while True:
#     escolha = int(input('Digite um numero entre 1-20: '))
#     if 0 <= escolha <= 20:
#         break
#     print('Tente novamente.', end=' ')
# print(f'Foi digitado o numero \033[1;33m{numeros[escolha]}\033[m')
while True:
    escolha = int(input('Digite um numero entre 1-20: '))
    con = ' '
    if 0 <= escolha <= 20:
        print(f'Foi digitado o numero \033[1;33m{numeros[escolha]}\033[m')
    else:
        print('Fora de escala.', end=' ')
    while con not in 'SsNn':
        con = str(input('Deseja continuar[s/n]: '))[0]
    if con in 'Nn':
        break
