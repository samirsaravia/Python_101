from random import randint
from time import sleep
from operator import itemgetter
jogo: dict = {'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou: {v}')
    sleep(1)
# itemgetter ordena se for a parte 0(key) ou 1 (value).
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking')
for p, jogador in enumerate(ranking):
    # a lista ranking tem tuplas dentro.
    print(f'  -  {p + 1}° lugar é para o {jogador[0]} com {jogador[1]}')
    sleep(0.5)
