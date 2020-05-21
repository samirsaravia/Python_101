def li():
    print('---' * 10)


def area(largura, comprimento):
    are = largura * comprimento
    print(f'A área de um terreno de {largura:.2f} X {comprimento:.2f} =  {are:.2f}m²')


print('Controle de terrenos')
li()
a = float(input('largura (m): '))
b = float(input('Comprimento (m): '))
area(a, b)
