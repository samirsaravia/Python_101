nota1 = float(input('Digite a primeira nota: ').strip())
nota2 = float(input('Digite a segunda nota: ').strip())
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média {:.1f} ,abaixo de 5.0: \033[0;31mREPROVADO\033[m'.format(media))
elif media < 6.9:
    print('Média {:.1f},entre 5.0 e 6.9: \033[0;33mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Média {:.1f},acima de  7.0: \033[0;34mAPROVADO\033[m'.format(media))
