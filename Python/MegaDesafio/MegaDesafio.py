def percorre_duracoes(duracoes, somatorios):
    remover_itens = []
    somatorio_tempo = 0.0
    for i in range(0, 1):
        somatorio_tempo += duracoes[i]
        for j in range(i, len(duracoes)):
            if i != j:
                if somatorio_tempo + duracoes[j] > 3.0:
                    continue
                else:
                    somatorio_tempo += duracoes[j]
                    print(somatorio_tempo)
                    remover_itens.append(j)
        remover_itens.append(i)
        somatorios.append(somatorio_tempo)
        somatorio_tempo = 0.0
    for i in remover_itens:
        duracoes.pop(i)



def acharMinimoDeDias(duracoes):
    somatorios = []
    percorre_duracoes(duracoes, somatorios)
    while len(duracoes) > 0:
        percorre_duracoes(duracoes, somatorios)
    else:
        print(somatorios)
        dias = len(somatorios)
        print(f'Dias para concluir: {len(somatorios)}')
    return dias


duracoes = [ 1.01]
acharMinimoDeDias(duracoes)