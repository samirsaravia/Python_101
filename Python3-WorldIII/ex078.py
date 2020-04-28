valores: list = list()
maior = menor = 0
for cv in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cv}: ')))
    maior = max(valores)
    menor = min(valores)
    # if cv == 0:
    #     maior = menor = valores[cv]
    # else:
    #     if valores[cv] > maior:
    #         maior = valores[cv]
    #     if valores[cv] < menor:
    #         menor = valores[cv]
print('---' * 15)
print(f'O maior valor é {maior} na posição :', end=' ')
for i, nv in enumerate(valores):
    if nv == maior:
        print(i, end=', ')
print(f'\nO menor valor é {menor} na posição ', end=' ')
for i, nv in enumerate(valores):
    if nv == menor:
        print(i, end=', ')
print()
print(type(valores))
