def notas(*n, sit=False):
    """
    -> Verifica as notas:
    :param n: notas que foram registradas
    :param sit: (opcional) situação: Boa, Regular, Ruim , segundo a média
    :return: dicionário : maior, menor, total de notas, media e situação(opcional)
    """
    aluno: dict = dict()
    maior = menor = soma = 0
    # co = contador
    # cn = cada número
    for co, cn in enumerate(n):
        soma += cn
        if co == 0:
            maior = cn
            menor = cn
        else:
            if cn > maior:
                maior = cn
            if cn < menor:
                menor = cn
        aluno['maior'] = maior
        aluno['menor'] = menor
        aluno['total'] = co + 1
        aluno['media'] = soma / aluno['total']
    if sit:
        if aluno['media'] > 6:
            situacao = 'Boa'.upper()
        elif aluno['media'] < 4:
            situacao = 'Ruim'.upper()
        else:
            situacao = 'regular'.upper()
        aluno['situação'] = situacao
    return aluno
    

# programa principal
r = notas(6.5, 8, 4.5, 7, 9.4, 2, 1, sit=True)
print(r)
