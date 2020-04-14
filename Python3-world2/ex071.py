cedula = 100
total_cedulas = 0
saque = int(input('Valor de saque: '))
montante = saque
while True:
    if montante >= cedula:
        montante -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de cedulas de {cedula}: {total_cedulas} ')
        if cedula == 100:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if montante == 0:
            break
