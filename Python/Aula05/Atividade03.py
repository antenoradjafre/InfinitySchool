class Produto:
    def __init__(self, codigo, nome, valor):
        self.__codigo = codigo
        self.__nome = nome
        self.__valor = valor

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

    def __str__(self):
        return f'Produto: {self.get_codigo()} - {self.get_nome()} - Valor: {self.get_valor():.2f}'


class Carrinho:
    def __init__(self):
        self.__produtos = []

    def get_produtos(self):
        return self.__produtos

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def listar_produtos(self):
        for produto in self.get_produtos():
            print(produto)

    def valor_carrinho(self):
        valor = 0.0
        for produto in self.get_produtos():
            valor += produto.get_valor()
        return valor


produto1 = Produto('123', 'Chocolate', 10.5)
produto2 = Produto('456', 'Sorvete', 20)
produto3 = Produto('789', 'Pizza', 50.75)
carrinho = Carrinho()
carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)

carrinho.listar_produtos()

print(f'Valor total do carrinho: {carrinho.valor_carrinho()}')