class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def depositar(self, saldo):
        if saldo > 0.0:
            self.saldo += saldo
        else:
            print("Valor inválido")


def cadastroConta():
    agencia = input("Digite sua agencia: ")
    conta = input("Digite sua conta: ")
    saldo = float(input("Digite seu saldo: "))
    favorecido = input("Digite o favorecido: ")
    conta = ContaCorrente(agencia, conta, saldo, favorecido)
    return conta


contaCorrente = cadastroConta()
print(contaCorrente.favorecido)
print(contaCorrente.agencia)
print(contaCorrente.conta)
print(contaCorrente.saldo)

deposito = float(input("Quando deseja depositar ? "))
contaCorrente.depositar(deposito)
print(contaCorrente.saldo)
