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


class Empresa:
    def __init__(self, razao, cnpj):
        self.__razao = razao
        self.__cnpj = cnpj
        self.__enderecos=[]

    def get_enderecos(self):
        return self.__enderecos

    def imprime_enderecos(self):
        for endereco in self.get_enderecos():
            print(endereco)

    def adiciona_endereco(self, rua, bairro, cidade):
        endereco = Endereco(rua, bairro, cidade)
        self.__enderecos.append(endereco)


e1 = Empresa('Razao1', 'CNPJ')
e1.adiciona_endereco('Rua 1', 'Bairro 1', 'Cidade')
e1.adiciona_endereco('Rua 2', 'Bairro 2', 'Cidade')
e1.adiciona_endereco('Rua 3', 'Bairro 3', 'Cidade')

e1.imprime_enderecos()