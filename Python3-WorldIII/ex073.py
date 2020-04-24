print('Brasileirão'.upper())
times = 'Flamengo', 'Santos', 'Palmeiras','Grêmio', 'Atletico-P', 'São Paulo','Internacional', 'Corinthians', \
        'Fortaleza', 'Goias', 'Bahia', 'Vasco da Gama', 'Atletico-Mineiro', 'Fluminense', 'Botafogo', 'Ceará', \
        'Cruzeiro', 'Csa', 'Chapecoense', 'Avai'
print(f'\033[1;33mLista do Brasileirão:\033[m {times}')
print(f'\033[1;33mOs primeiros 5 times são\033[m: \033[1;32m{times[:5]}\033[m')
print(f'\033[1;33mOs ultimos 4 times são:\033[m \033[1;31m{times[-4:]}\033[m')
print(f'\033[1;33mOs times em ordem alfabetica:\033[m {sorted(times)}')
print(f'\033[1;33mA\'Chapecoense\' encontra-se na posição: \033[m{times.index("Chapecoense") + 1}')
