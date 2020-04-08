print('-=-' * 10)
title = 'Tabuada'.upper()
print(f'\033[7;30m{title:^30}\033[m')
print('-=-' * 10)
while True:
    cont = 0
    escolha = int(input('escolha o número : '))
    if escolha < 0:
        break
    while cont != 10:
        cont += 1
        produto = escolha * cont
        print(f'{escolha:^5} X {cont:^3} = \033[1;33m{produto:>3}\033[m')
print('FIM')
