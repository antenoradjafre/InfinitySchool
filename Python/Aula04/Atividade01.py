class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__cpf = ''


    def cadastra_nome(self, nome):
        self.__nome = nome



    def cadastra_idade(self, idade):
        self.__idade = idade



    def cadastra_cfp(self, cpf):
        self.__cpf = cpf


    def __str__(self):
        return f'Nome: {self.__nome} - Idade: {self.__idade} - cpf: {self.__cpf}'



pessoa = Pessoa()
print(pessoa)
pessoa.cadastra_cfp('123456789')
pessoa.cadastra_nome('Joao Ninguem')
pessoa.cadastra_idade(23)
print(pessoa)



