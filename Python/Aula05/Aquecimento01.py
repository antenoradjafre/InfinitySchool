class Paciente:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def envelhecer(self):
        self.__idade += 1

    def get_idade(self):
        return self.__idade


p1 = Paciente('Antenor', 20, '123456')

print(p1.get_idade())
p1.envelhecer()
print(p1.get_idade())

