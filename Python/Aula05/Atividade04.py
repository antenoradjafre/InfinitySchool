class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua

    def get_bairro(self):
        return self.__bairro

    def get_cidadee(self):
        return self.__cidade

    def __str__(self):
        return f'Rua: {self.get_rua()} - Bairro: {self.get_bairro()} - Cidade: {self.get_cidadee()}'


class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def preenche_endereco(self, rua, bairro, cidade):
        endereco = Endereco(rua, bairro, cidade)
        self.set_endereco(endereco)

    def imprime_dados(self):
        print(f'Pessoa: {self.get_nome()} Telefone: {self.get_cpf()} Mora em: {self.get_endereco()}')


class ContaBancaria:
    def __init__(self, agencia, conta, saldo, favorecido, limite):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        self.__favorecido = favorecido
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def sacar(self, valor):
        limite = self.get_limite()
        if valor > limite:
            print(f'Saldo insuficiente: {self.get_saldo()}')
        else:
            self.set_saldo(self.get_saldo() - valor)

