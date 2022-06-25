class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def engordar(self, valor):
        self.peso += valor

    def emagrecer(self, valor):
        if valor < self.peso:
            self.peso -= valor
        else:
            print("Valor não pode ser menor que o peso total ")

    def crescer(self, valor):
        self.altura += valor

    def envelhecer(self, valor):
        if valor > 0:
            nova_idade = self.idade + valor
            if self.idade < 21:
                if nova_idade > 21:
                    self.crescer((nova_idade-self.idade)*0.5)
                else:
                    crescer = valor*0.5
                    self.crescer(crescer)
            self.idade += valor

pessoa1 = Pessoa("Antenor", 10, 100, 100)
print(pessoa1.altura)
pessoa1.envelhecer(10)
print(pessoa1.altura)

    



