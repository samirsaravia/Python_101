print(f'\033[7;30m{"Achando vogais nas palavras":^45}\033[m')
library: tuple = ('fofo', 'celular', 'computador', 'ipad', 'puff', 'sofa', 'travesseiro', 'almofada', 'cadeira', 'mesa',
                  'lampada', 'ventilador', 'televisao', 'espelho', 'tecla')
for li in library:
    print(f'\n{li:>19}{"":.<5}', end=' ')
    for palavra in li:
        if palavra in 'aeiou':
            print(f'{palavra}', end='')
        else:
            print(f'\033[1;31m{"x"}\033[m', end='')
print('\n', '---' * 15, '\n', '\033[1;31m---\033[m' * 15)
