numeros: list = [[], []]
# cn = cada numero
for cn in range(0, 7):
    valor: int = int(input(f'Digite o {cn + 1}° valor:  '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('___' * 15)
print(f'Os numeros pares foram: {sorted(numeros[0])}')
print(f'Os numeros ímpares foram: {sorted(numeros[1])}')
