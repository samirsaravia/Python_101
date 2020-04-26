lista: tuple = ('lapiz', 1.34, 'Borracha', 2, 'Caderno', 32.45, 'Estojo', 25, 'Compasso', 10, 'Mochila', 120,
                'Caneta', 23.97, 'Livro', 123, 'Regra', 2.75)
print('---' * 15)
print(f'\033[7;30m{"Listagem de Preços":^45}\033[m')
print('---' * 15)
for tabela in range(0, len(lista), 2):
    print(f'{lista[tabela]:.<33}R$  {lista[tabela + 1]:>8.2f}')
print('---' * 15)
