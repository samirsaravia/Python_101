from time import sleep


def maior(* valor):
    print(f'Analisando o maior...')
    sleep(1.4)
    print(f'    Foram informados: {len(valor)} valores.')
    pos = m = 0
    for num in valor:
        sleep(0.5)
        print(f'    {num}', end='', flush=True)
        pos += 1
        if pos == 0:
            m = num
        else:
            if num > m:
                m = num
    print()
    sleep(1.5)
    print(f'O maior valor digitado é: {m}')
    sleep(2)
    print('---' * 15)


maior(11, 2, 3, 7)
maior(6, 5)
maior(7)
maior(1, 0, 2, 5, 4, 7, 8, 11, 10, 14, 12)
maior()
