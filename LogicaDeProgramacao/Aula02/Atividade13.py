numero = int(input("Digite um numero: "))
dividido = int(numero/2)
print(dividido)
dividido += dividido
print(dividido)

if numero == dividido:
    print("Número é par")
else:
    print("Número é ímpar")
    