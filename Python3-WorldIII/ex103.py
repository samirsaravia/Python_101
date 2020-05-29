def ficha(gols, nome='<desconhecido>'):
    print(f'O jogador {nome} marcou {gols} gol(s).')


# programa principal
nome_jog: str = input('Nome: ').strip()
gol_marcado = input('Gol(s) Marcado(s) : ')
if gol_marcado.isdigit():
    gol_marcado = int(gol_marcado)
else:
    gol_marcado = 0
if nome_jog == '':
    ficha(gols=gol_marcado)
else:
    ficha(gol_marcado, nome_jog)
