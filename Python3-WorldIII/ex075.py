print('-=-' * 15)
quest: tuple = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
                int(input('Digite um valor: ')))
print('-=-' * 15)
print(f'o valores digitados foram: \033[1;33m{quest}\033[m')
print(f'O numero 9 apareceu \033[1;33m{quest.count(9)}\033[m vezes.')
if quest.count(3) == 0:
    print(f'O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O número 3 aparece na posição {quest.index(3) + 1}')
print('Os valores pares são: ', end=' ')
for valores in quest:
    if valores % 2 == 0:
        print(f'{valores}', end=' ')

