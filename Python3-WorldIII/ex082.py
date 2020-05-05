from time import sleep
# li_val = lista de valores
# li_par = lista de pares
# li_imp = lista de ímpares
li_val: list = list()
while True:
    val = input('Digite um valor:  ')
    if val.isdigit():
        val = int(val)
        if val not in li_val:
            li_val.append(val)
        else:
            print('Valor já foi digitado.')
        flag = ' '
        while flag not in 'sSnN':
            flag: str = str(input('Desesja continuar [S/N]: '))[0]
        if flag in 'Nn':
            break
    else:
        print('Valor não reconhecido.')
li_par: list = li_val[:]
li_imp: list = li_val[:]
for sub_li in li_val:
    if sub_li % 2 == 0:
        li_imp.remove(sub_li)
    else:
        li_par.remove(sub_li)
sleep(0.5)
print('___' * 15)
print(f'Lista com todos os valores: {li_val}')
if len(li_par) > 0:
    print(f'Lista com numeros pares {li_par}')
else:
    print('Não há números pares')
if len(li_imp) > 0:
    print(f'Lista com números ímpares {li_imp}')
else:
    print('Não há números ímpares.')
