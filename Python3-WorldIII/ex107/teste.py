import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade do preço é: {moeda.metade(p)}')
print(f'O preço em dobro é: {moeda.dobro(p)}')
print(f'O preço -13% é : {moeda.reducir(p, 13)}')
print(f'O preço +15% é: {moeda.aumentar(p, 15)}')
