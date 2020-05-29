from time import sleep


def lin():
    print('-=' * 15)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        lin()
        sleep(3)
        for c in range(i, f + 1, p):
            sleep(0.3)
            print(c, end=' ')
        print()
        sleep(2)
        print("<<<FIM>>>")
        lin()
    else:
        sleep(1.8)
        print(f'Contagem de {i} até {f} de {p} em {p}')
        sleep(3)
        for c in range(i, f - 1, - p):
            sleep(0.3)
            print(c, end=' ')
        print()
        sleep(2)
        print('<<<FIM>>>')
        lin()


# OBS: se for usado o while, o sleep precisa ligar o flush=True para evitar o buffer que
# store(data) enquanto é processada a info,ou uma memoria temporaria.
contador(1, 10, 1)
contador(10, 0, 1)
print('Agora é a sua vez!')
sleep(1.2)
contador(int(input('inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
