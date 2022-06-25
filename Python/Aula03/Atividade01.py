class ContaCorrente:
    def __init__(self, agencia, conta, saldo, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.favorecido = favorecido

    def __repr__(self):
        return (
            f"Agencia: {self.agencia} - Conta: {self.conta} - Saldo: {self.saldo:.2f} - Favorecido: {self.favorecido}")


conta1 = ContaCorrente(6542, 102021, 22.5, "Eu")
print(conta1)
