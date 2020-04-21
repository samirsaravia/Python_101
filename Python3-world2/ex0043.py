peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    resultado = 'Falta de peso'
elif 18.5 < imc < 25:
    resultado = 'Peso ideal'
elif 25 < imc < 30:
    resultado = 'Sobrepeso'
elif 30 < imc < 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade mórbida'
print('Seu IMC é: {}{:.2f}{}Kg/m²'.format('\033[0;33m', imc, '\033[m'))
print('Você está com: \033[4;34m{}\033[m'.format(resultado))
