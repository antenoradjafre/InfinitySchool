class Endereco:
    def __init__(self, rua, bairro, cidade):
        self.__rua = rua
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
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = Endereco('', '', '')

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def preenche_endereco(self, rua, bairro, cidade):
        endereco = Endereco(rua, bairro, cidade)
        self.set_endereco(endereco)

    def imprime_dados(self):
        print(f'Pessoa: {self.get_nome()} Telefone: {self.get_telefone()} Mora em: {self.get_endereco()}')


pessoa = Pessoa('Antenor', '(85)99595-5656')
pessoa.preenche_endereco('Rua A', 'Marapongs', 'Fortaleza')

pessoa.imprime_dados()