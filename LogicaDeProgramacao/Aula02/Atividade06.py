peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = (peso/(altura**2))
print(imc)

if imc >= 40:
    print("Alerta: Obesidade Mórbida")
elif 30 <= imc < 39.9:
    print("Obesidade Tipo 1")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 18.5 <= imc < 24.9:
    print("Normal")
else:
    print("Abaixo do Peso")

