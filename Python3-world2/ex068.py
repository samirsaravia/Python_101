import random
title = 'par ou ímpar'.upper()
print('~~' * 10)
print(f'\033[7;30m{title:^20}\033[m')
print('~~' * 10)
# poi = par ou impar
# vop = vitoria ou perda
poi = vop = ''
cont = 0
while True:
    cont += 1
    escolha_numero = int(input('Digite um número: '))
    escolha_parinpar = str(input('Par ou Impar[P/I]: ')).strip().upper()[0]
    en = escolha_numero
    epi = escolha_parinpar
    # npc = numero do pc
    npc = random.randint(1, 100)
    soma = npc + en
    if soma % 2 == 0:
        poi = 'par'
    else:
        poi = 'ímpar'
    if soma % 2 == 0 and epi in 'Pp' or soma % 2 != 0 and epi in 'Ii':
        vop = '\033[1;32mganhou\033[m'
    else:
        vop = '\033[1;31mperdeu\033[m'
        break
    print(f'O numero escolhido pelo pc foi : {npc}')
    print(f'A soma foi: \033[1;33m{soma}\033[m')
    print(f'Você {vop}, deu \033[1;33m{poi}\033[m')
    print('---' * 10)
print(f'O numero escolhido pelo pc foi : {npc}')
print(f'A soma foi: \033[1;33m{soma}\033[m')
if cont > 1:
    print(f'Depois de {cont - 1} vezes seguidas, ', end='')
print(f'Você {vop}, deu \033[1;33m{poi}')
