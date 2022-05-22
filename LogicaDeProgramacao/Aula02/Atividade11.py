nomeAluno = input("Insira o nome do Aluno: ")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
media = (nota1+nota2)/2
print("Média é: ", media)

if media < 4.0:
    print(nomeAluno, "reprovado :/")
elif media >= 4.0 and media < 5.0:
    print(nomeAluno, "fará avaliação final")
elif media >= 5.0 and media < 7.0:
    print(nomeAluno, "aprovado com conceito B")
elif media > 7.0:
    print(nomeAluno, "aprovado com conceito A")

