title = 'produtos'.upper()
print(f'\033[7;30m{title:^30}\033[m')
print('---' * 10)
cont = total = preço_mais_m = preço_menor = 0
menor_nome_p = ''
while True:
    cont += 1
    nome: str = str(input('Nome do produto :  ')).strip().lower()
    preço: float = float(input('Preço R$: '))
    total += preço
    novo_preço = preço + preço_menor
    if preço > 10:
        preço_mais_m += 1
    
    if preço == novo_preço:
        menor_nome_p = nome
        preço_menor = preço
    else:
        if preço < preço_menor:
            menor_nome_p = nome
            preço_menor = preço
        
    pergunta: str = str(input('\033[1;33mDeseja continuar[S/N]:\033[m ')).strip().upper()[0]
    if pergunta in 'Nn':
        print('---' * 10)
        break
    print('---' * 10)
print(f'Total : R$ {total:.2f}')
print(f'Há {preço_mais_m} produtos acima de R$ 10')
print(f'O menor preço é: {menor_nome_p},R${preço_menor:.2f} ')
