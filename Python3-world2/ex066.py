cont = soma = 0
while True:
    numero = int(input('Digite um valor [999p/parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Foram digitados {cont} números e a soma de todos foi: {soma}')
