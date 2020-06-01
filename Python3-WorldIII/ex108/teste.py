import moeda

"""
moeda.__moeda__ = 1° moeda = módulo
__moeda__.moeda = func dentro do módulo moeda
__moeda__fun recebe (moeda:str = 'R$',preco=0)
"""
p = float(input('Digite o preço R$: '))
print(f'    -A metade do preço de {moeda.moeda(p)} = {moeda.moeda(moeda.metade(p))}')
print(f'    -O preço em dobro de {moeda.moeda(p)} = {moeda.moeda(moeda.dobro(p))}')
print(f'    -O preço -13% de {moeda.moeda(p)} = {moeda.moeda(moeda.reducir(p, 13))}')
print(f'    -O preço +15% de {moeda.moeda(p)} = {moeda.moeda(moeda.aumentar(p, 15))}')
