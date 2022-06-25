class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def depositar(self, valor):
        if valor > 0.0:
            self.saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor


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

for i in range(0, 5):
    deposito = float(input("Quando deseja depositar ? "))
    contaCorrente.depositar(deposito)
    i += 1

print(f'Saldo é: {contaCorrente.saldo}')

saque = float(input("Digite o valor a sacar: "))
contaCorrente.sacar(saque)

print(f'Saldo é: {contaCorrente.saldo}')