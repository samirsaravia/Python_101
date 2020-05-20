from time import sleep
jogadores: list = list()
gol_marcado: list = list()
jogador: dict = dict()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
    partidas = int(input(f'Quantas partidas jogou {jogador["nome"]}: '))
    print(f'{"Gols marcados":^45}'), print('---' * 15)
    for CadaJogo in range(1, partidas + 1):
        gols: int = int(input(f'    -Quantos gols marcou na partida {CadaJogo}: '))
        gol_marcado.append(gols)
    jogador['gols'] = gol_marcado[:]
    jogador['total'] = sum(gol_marcado[:])
    jogadores.append(jogador.copy())
    gol_marcado.clear()
    jogador.clear()
    while True:
        flag = str(input('Deseja continuar: ').strip())[0]
        if flag in 'SsNn':
            print('---' * 15)
            break
        else:
            print('Digite SIM ou NÃO')
    if flag in 'Nn':
        # termina o loop inteiro
        break
print(f'{"cod":<5}', end='')
print(f'{"nome":<15}', end='')
print(f'{"gols":<15}', end='')
print(f'{"total":<15}')
print('==' * 20)
# c == contador de jogador
# info = info do jogador
# c_info = cada info do jogador
for c, info in enumerate(jogadores):
    print(f'{c:<5}', end='')
    for c_info in info.values():
        print(f'{str(c_info):<15}', end='')
    print()
# loop para mostrar dados de cada jogador
while True:
    dado_jogador = int(input('Mostrar dados de qual jogador(999 parar): '))
    if dado_jogador <= len(jogadores) - 1:
        print(f'Levantamento do jogador {jogadores[dado_jogador]["nome"]}')
        print('---' * 15)
        for cada_jogo, cada_gol in enumerate(jogadores[dado_jogador]['gols']):
            print(f'    -No jogo {cada_jogo + 1} fez {cada_gol} gols.')
        print('---' * 15)
    else:
        if dado_jogador == 999:
            print('<<< Finalizando >>>...')
            sleep(1.5)
            break
        else:
            print('Não existe código desse jogador')
