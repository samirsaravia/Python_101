val: list = list()
for sv in range(0, 5):
    valor_digitado = input('Digite um valor: ')
    if valor_digitado.isdigit():
        valor_digitado = int(valor_digitado)
        if sv == 0 or val == list() or valor_digitado > val[-1]:
            val.append(valor_digitado)
        else:
            # barrer o vetor inteiro com posição
            posição = 0
            while posição < len(val):
                if valor_digitado < val[posição]:
                    val.insert(posição, valor_digitado)
                    break
                posição += 1
    else:
        print('Digito não reconhecido')
        
print(val)
cont = 0
for pos in val:
    cont += 1
if cont < 5:
    letras = 5 - cont
    print(f'Foram digitados só {cont} digitos númericos e {letras} digitos com palavras ou espaços vazios')
else:
    print(f'Foram digitados {cont} digitos')