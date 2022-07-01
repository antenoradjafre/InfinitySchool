class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__cpf = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def __str__(self):
        nome = self.get_nome()
        idade = self.get_idade()
        cpf = self.get_cpf()
        return f'Nome: {nome} - Idade: {idade} - cpf: {cpf}'


pessoa = Pessoa()
print(pessoa)
pessoa.set_cpf('123456789')
pessoa.set_nome('Joao Ninguem')
pessoa.set_idade(23)
print(pessoa)
