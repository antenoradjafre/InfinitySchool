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

    def transferencia(self, contaCorrente, valor):
        self.sacar(valor)
        contaCorrente.depositar(valor)

    def mostraConta(self):
        print(f"Conta: {self.conta} de {self.favorecido} possui saldo: {self.saldo}")


def cadastroConta():
    agencia = input("Digite sua agencia: ")
    conta = input("Digite sua conta: ")
    saldo = float(input("Digite seu saldo: "))
    favorecido = input("Digite o favorecido: ")
    conta = ContaCorrente(agencia, conta, saldo, favorecido)
    return conta


def realizaDepositos(contaCorrente):
    for i in range(0, 5):
        deposito = float(input(f"Quando deseja depositar a conta  {contaCorrente.conta} ? "))
        contaCorrente.depositar(deposito)
        i += 1


def realizaSaques(contaCorrente):
    for i in range(0, 5):
        saque = float(input(f"Quando deseja sacar da conta {contaCorrente.conta} ? "))
        contaCorrente.depositar(saque)
        i += 1


contaCorrente1 = cadastroConta()
contaCorrente2 = cadastroConta()
realizaDepositos(contaCorrente1)
realizaDepositos(contaCorrente2)
realizaSaques(contaCorrente1)
realizaSaques(contaCorrente2)
valor_transferencia = float(input("Insira o valor a transferir: "))

contaCorrente1.transferencia(contaCorrente2, valor_transferencia)

contaCorrente1.mostraConta()
contaCorrente2.mostraConta()
