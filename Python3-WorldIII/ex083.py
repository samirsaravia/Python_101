li_index: list = list()
usuario = input('Digite uma expressão: ')
for sub_us in usuario:
    if '(' in sub_us:
        li_index.append(sub_us)
    elif ')' in sub_us:
        if len(li_index) == 0 or ')' in li_index:
            li_index.append(sub_us)
        else:
            li_index.pop()
if len(li_index) == 0:
    print('Expressão correta!')
else:
    print('Expressão incorreta!')
    if '(' in li_index:
        print('Há parentesis aberto sem fechar.')
    elif ')' in li_index:
        print('Há parentesis fechado sem ter sido aberto')
