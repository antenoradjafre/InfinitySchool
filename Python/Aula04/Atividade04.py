class Funcionario:
    def __init__(self):
        self.__nome = ''
        self.__salario = 0.0
        self.__matricula = ''
        self.__funcao = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        if salario > self.__salario:
            self.__salario = salario
        else:
            print('Novo salario não pode ser inferior ao atual')

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    def aumentar_salario(self):
        salario = self.__salario
        aumento = 20 * salario / 100
        novo_salario = salario + aumento
        self.salario = novo_salario


