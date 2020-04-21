print('---' * 8)
print('\033[7;30mANALISANDO TRIÂNGULOS\033[m')
print('---' * 8)
a = float(input('Digite o valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite o ultimo valor: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Com o valor {}, {}, {}: {}PODE{} formar um triângulo.'.format(a, b, c, '\033[1;33m', '\033[m'))
    if a == b == c:
        tr = 'EQUILATERO'
        conc = 'Todos os lados iguais.'
    elif a == b and b != c or b == c and c != a or a == c and c != b:
        tr = 'ISÓSCELES'
        conc = 'Só dois lados iguais.'
    else:
        tr = 'ESCALENO'
        conc = 'Nenhum lado é igual.'
    print('E o triangulo a formar é : {}{}{}'.format('\033[4;33m', tr, '\033[m'))
    print(tr + ':  {}'.format(conc))

else:
    print('\033[1;31mNÃO\033[m pode formar um triângulo.')

