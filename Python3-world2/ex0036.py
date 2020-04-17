import time
from math import ceil
casa = int(input('Valor da casa: ').strip())
salario = float(input('Qual o seu salario: ').strip())
ano = int(input('Quantos anos pretende pagar: ').strip())
usosalario = salario * 30 / 100
meses = ano * 12
print('Calculando . . .')
time.sleep(3)
if casa / meses <= usosalario and ano <= 30 and casa > 50000:
    parcela = casa / meses
    print('O valor de cada parcela será : R${:.2f}'.format(ceil(parcela)))
    print('Em {} parcelas. '.format(meses))
elif casa / meses > usosalario and ano <= 30:
    parcela = casa / meses
    print('O valor de cada parcela seria: R${:.2f}'.format(parcela))
    print('mas a seu orçamento de 30%max.de um salario é de : R${:.2f}'.format(usosalario))
    print('Faltando : R${:.2f} por parcela.'.format(parcela - usosalario))
    print('O que \033[0;31mNÃO\033[m deixa-o qualificado para o emprestimo')
else:
    print('\033[4;31mSinto muito, ainda não há como qualificarlo para o emprestimo.')
