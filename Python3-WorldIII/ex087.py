matriz: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
list_pares = list()
col_tres = list()
col_dois = list()
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}:{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            list_pares.append(matriz[linha][coluna])
        if coluna == 2:
            col_tres.append(matriz[linha][coluna])
        if coluna == 1:
            col_dois.append(matriz[linha][coluna])
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ', end='')
    print()
print(f'A soma dos numeros pares digitados é: {sum(list_pares)}')
print(f'A soma da terceira coluna é: {sum(col_tres)}')
print(f'O maior valor da coluna 2 é: {max(col_dois)}')
print(col_dois)
print(col_tres)
