a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
if a > b:
    print('O número \033[4;31m{}\033[m é maior que {}.'.format(a, b))
elif b > a:
    print('o número \033[0;33m{}\033[m é maior que {}.'.format(b, a))
else:
    print('Não existe número maior, os dois são iguais.')
