data = int(input('Digite o ano de nascimento: ').strip())
idade = 2020 - data
if idade < 16:
    print('Ainda vai se alistar ao seriço militar.')
    print('Faltam {} ano/s'.format(17 - idade))
    print('Você vai se alistar no ano {}-{}'.format(data + 17, data + 18))
elif 16 < idade <= 18:
    print('Você está na hora de se alistar.')
else:
    print('Você ja passou do tempo do alistamento.')
    print('com {} ano/s.'.format(idade - 18))
    print('Você tinha que se alistar no ano {} - {}'.format(data + 17, data + 18))
