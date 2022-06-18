def cadastro():
    alunos = {}
    notas = []
    while True:
        nome = input("Insira o nome do Aluno: ")
        if nome == "":
            break
        else:
            if nome not in alunos:
                nota1 = float(input("Insira a nota 1: "))
                nota2 = float(input("Insira a nota 2: "))
                notas.append(nota1)
                notas.append(nota2)
                alunos[nome] = []
                alunos[nome].append(nota1)
                alunos[nome].append(nota2)
            else:
                print("Aluno ja cadastrado")
                continue
    return alunos


def calcula_media(alunos, aluno):
    values = alunos[aluno]
    soma = 0
    for i in range(0, len(values)):
        soma += values[i]
    media = soma/len(values)
    return media


alunos = cadastro()
for nome_do_aluno in alunos.keys():
    media = calcula_media(alunos, nome_do_aluno)
    print(f"A media de {nome_do_aluno} é {media:.2f}")


