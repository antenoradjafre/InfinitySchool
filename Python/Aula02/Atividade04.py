def calcula_aprovados(alunos, medias):
    aprovados: [str] = []
    for i in range(0, len(alunos)):
        if medias[i] > 7:
            aprovados.insert(i, alunos[i])
    return aprovados


alunos: [str] = []
medias: [float] = []

for i in range(0, 10):
    nome = input("Insira o nome do aluno: ")
    media = float(input("Insira a média do aluno: "))
    alunos.insert(i, nome)
    medias.insert(i, media)

print(calcula_aprovados(alunos, medias))
