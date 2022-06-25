class CarrinhoDeCompras:
    def __init__(self, vip):
        self.produtos = []
        self.precos = []
        self.vip = vip
        self.total = 0.0

    def adicionarProduto(self, produto, preco):
        self.produtos.append(produto)
        self.precos.append(preco)
        self.total += preco

    def exibirTotalCompra(self):
        if self.vip:
            desconto = (0.10*self.total)
            print(f"Desconto: {desconto:.2f}")
            self.total -= desconto

        produtos = self.produtos
        precos = self.precos
        for i in range(0,len(produtos)):
            print(f"Produto: {produtos[i]} - Preço: {precos[i]}")
        print(f"Total: {self.total}")


carrinho = CarrinhoDeCompras(False)
carrinho.adicionarProduto("Monster", 10.0)
carrinho.adicionarProduto("Coca", 3.0)
carrinho.adicionarProduto("Pizza", 20.0)
carrinho.exibirTotalCompra()

carrinho2 = CarrinhoDeCompras(True)
carrinho2.adicionarProduto("Monster", 10.0)
carrinho2.adicionarProduto("Coca", 3.0)
carrinho2.adicionarProduto("Pizza", 20.0)
carrinho2.exibirTotalCompra()

