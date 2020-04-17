from math import floor
from time import sleep
tempo = int(input('De aqui a quantos dias: ').strip())
ka = float(input('Digite o valor da constante "a": ').strip())
kb = float(input('Digite o valor da constante "b": ').strip())
porc = float(input('Qual a porcentagem de pessoas na UTI:  ').strip())
infectados = (ka * tempo ** 2) + (kb * tempo)
calporc = infectados * porc / 100
print('Calculando ...')
sleep(3)
print('O número de pessoas \033[0;31minfectadas\033[m de aqui a {}dias, será de: \033[4;31m{:.0f}\033[m'.format(tempo, infectados))
print('o número possível de pessoas na UTI,ao \033[1;33m{}%\033[m, pode alcançar as: \033[4;31m{}\033[m'.format(porc, floor(calporc)))
print('O/os obito/s segundo pessoas na UTI: \033[4;31m{:.2f}\033[m'.format(infectados * 11 / 904))
