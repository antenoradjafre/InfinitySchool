vel = int(input("Insira a velocidade de um carro: "))
if vel > 120:
    print("VUADO!!!")
elif vel > 80 and vel <= 120:
    print("Muito Rápido")
elif vel > 60 and vel <= 80:
    print("Alta Velocidade")
else:
    print("Velocidade Permitida")
    