# matriz: list = [[], [], []]
# suporte: list = []
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz)):
#         valor = int(input(f'Digite um valor[{linha}:{coluna}]:  '))
#         if linha == 0:
#             suporte.append(valor)
#             matriz[0].append(suporte[:])
#             suporte.clear()
#         elif linha == 1:
#             suporte.append(valor)
#             matriz[1].append(suporte[:])
#             suporte.clear()
#         elif linha == 2:
#             suporte.append(valor)
#             matriz[2].append(suporte[:])
#             suporte.clear()
# for linha in range(len(matriz)):
#     for coluna in range(len(matriz)):
#         print(f'  {matriz[linha][coluna]}', end='')
#     print()
matriz: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número[{l}:{c}]: '))
print('---' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'  [{matriz[l][c]:^7}]  ', end='')
    print()
