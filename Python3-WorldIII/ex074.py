import random
numeros: tuple = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
                  random.randint(1, 100))
print()
print('os numeros sorteado são'.upper())
print('---' * 10)
for subn in numeros:
    print('\033[1;33m', subn, end='')
print(f'\033[m\nO numero maior é : {max(numeros)}')
print(f'O numero menor é: {min(numeros)}')
