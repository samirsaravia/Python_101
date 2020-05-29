from random import randint


def sorteia():
    for i in range(0, 5):
        sorteio = randint(1, 20)
        numeros.append(sorteio)


def somapar():
    somador = 0
    for i in numeros:
        if i % 2 == 0:
            somador += i
    print(somador)


numeros: list = list()
sorteia()
print(f'Os números sorteados foram: {numeros}')
print(f'    -A soma dos números pares é: ', end='')
somapar()
