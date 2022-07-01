class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = 0
        self.__cpf = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade} - cpf: {self.cpf}'


pessoa = Pessoa()
print(pessoa)
pessoa.cpf ='123456789'
pessoa.nome = 'Joao Ninguem'
pessoa.idade = 23
print(pessoa)
