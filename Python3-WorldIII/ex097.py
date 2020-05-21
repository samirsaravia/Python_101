lista_frase: list = list()
for i in range(0, 3):
    if i == 0:
        frase = str(input('Digite uma frase: ')).strip().capitalize()
    else:
        frase = str(input('Digite mais uma frase: ').strip().capitalize())
    lista_frase.append(frase)
for cl in lista_frase:
    def li():
        tan = len(cl) + 4
        print('~' * tan)


    li()
    print(f'  {cl}')
    li()
