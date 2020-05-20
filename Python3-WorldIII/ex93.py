Jogador: dict = dict()
gols: list = list()
Jogador['nome'] = str(input('Nome do Jogador: ')).upper()
indicador_jogos = int(input(f'Quantas partidas {Jogador["nome"]} jogou: '))
for g in range(1, indicador_jogos + 1):
    gol_marcado = int(input(f'Quantos gols foi marcado na {g}° partida: '))
    gols.append(gol_marcado)
    Jogador['gols'] = gols
Jogador['Total'] = sum(gols)
print('==' * 15)
print(f'O jogador {Jogador["nome"]}: jogou {indicador_jogos} partidas')
for q, g in enumerate(gols):
    print(f'    =>Na partida {q + 1} fez: {g} gols.')
print(f'Foi um total de {Jogador["Total"]} gols.')

