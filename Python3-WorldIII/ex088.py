import random
from time import sleep
print('===' * 15)
print(f'{"Jogos da MegaSena":^45}')
print('===' * 15)
usuario: int = int(input('Quantos jogos quere gerar:  '))
print('---' * 15)
print(f'Sorteando {usuario} jogos...')
cont = 0
for g in range(0, usuario):
    jogos: list = list()
    while len(jogos) < 6:
        cont += 1
        gerando = random.randint(1, 60)
        if cont == 0:
            jogos.append(gerando)
        else:
            if gerando in jogos:
                random.randint(1, 60)
            else:
                jogos.append(gerando)
    sleep(2)
    print(f'Jogo {g + 1}: {jogos} ')
    jogos.clear()
