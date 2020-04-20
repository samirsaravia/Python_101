import random
import time
print('--' * 10)
print('JOGO DO JAKEMPO')
print('--' * 10)
print('1. pedra'
      '\n2. papel'
      '\n3. tesoura')
user_data = str(input('Escreva qual você escolhe:\n>>>')).strip().lower()
time.sleep(0.5)
print('\033[1;33mJJJJJJJAAAA\033[m')
time.sleep(1)
print('\033[1;34mKKKEEEEM\033[m')
time.sleep(1)
print('\033[0;35mPPPPPOOOOO!!!\033[m')
time.sleep(0.5)
source_data = ['pedra', 'papel', 'tesoura']
choice = random.choice(source_data)
if user_data == 'papel' and choice == 'pedra':
    print('Você ganhou dessa vez!'.upper())
elif user_data == 'pedra' and choice == 'tesoura':
    print('Não acredito você ganhou!!'.upper())
elif user_data == 'tesoura' and choice == 'papel':
    print('Que sorte você ganhou!'.upper())
elif user_data == choice:
    print('Foi empate dessa vez!!')
    print('tambem, ', end=' ')
else:
    print('Eu ganhei dessa vez!!!')
    print('EU ESCOLHÍ {}{}'.format('\033[0;33m', choice.upper()))
    time.sleep(4.5)
    print('\033[0;33mMais uma??...'), exit()
print('Eu escolhi {}{}'.format('\033[0;33m', choice.upper()))
