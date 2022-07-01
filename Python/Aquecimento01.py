class Carro:
    def __init__(self, modelo, ano, velocidade, ligado, automatico):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico

    def ligar(self):
        self.ligado = True

    def acelerar(self, valor):
        if self.velocidade + valor > 120:
            print("Valor não suportado, velocidade máxima ultrapassada")
        else:
            self.velocidade += valor

    def checarMarcha(self):
        if self.velocidade <= 20.0:
            return "1ª Marcha"
        elif 20 < self.velocidade <= 30:
            return "2ª Marcha"
        elif 30 < self.velocidade <= 35:
            return "3ª Marcha"
        elif 35 < self.velocidade <= 45:
            return "4ª Marcha"
        else:
            return "5ª Marcha"


carro = Carro('palio', 2015, 120, True, False)
print(carro.checarMarcha())



