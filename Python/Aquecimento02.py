class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.semestre = 'primeiro'
        self.media = 0.0


    def calcular_media(self, nota1, nota2):
        media = (nota1 + nota2)/2
        self.media = media
        return media


    def passar_semestre(self):
        if self.media >= 7.0:
            return 'Aprovado'
        else:
            return 'Reprovado'


    def __str__(self):
        return f'Aluno {self.matricula} - {self.nome} - Semestre: {self.semestre} Média: {self.media}'




aluno = Aluno('123456789', 'Antenor')
print(aluno)
aluno.calcular_media(10.0, 5.0)
print(aluno.passar_semestre())
print(aluno)
