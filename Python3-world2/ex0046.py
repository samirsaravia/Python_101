import time
print('-=-' * 9)
print('Contagem regressiva')
print('-=-' * 9)
button = int(input('[1]START:  '))
if button == 1:
    time.sleep(1)
    for contagem in range(10, 0 - 1, -1):
        print(contagem)
        time.sleep(1)
print('fim')
