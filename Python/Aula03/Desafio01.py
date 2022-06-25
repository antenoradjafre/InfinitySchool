cursos = ["Programação", "Lógica", "Python"]


class Aluno:
    def __init__(self, matricula, nome, curso, notas):
        if curso in cursos:
            self.matricula = matricula
            self.nome = nome
            self.curso = curso
            self.notas = notas
        else:
            print(f"Aluno {nome} está num curso inválido")

    def cadastrarNota(self, nota):
        self.notas.append(nota)

    def calcularMedia(self):
        soma = 0
        notas = self.notas
        for i in range(0, len(notas)):
            soma += notas[i]
        return soma / len(notas)

    def mostrarResultado(self):
        media = self.calcularMedia()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"


aluno = Aluno("123456", "Antenor", "Python", [4.5, 7.7])
media = aluno.calcularMedia()
print(f"Media: {media}")
aluno.cadastrarNota(10)
media = aluno.calcularMedia()
print(f"Media: {media}")
print(aluno.mostrarResultado())

