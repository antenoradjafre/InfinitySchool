contador = 1
contadorPares = 0
contadorImpares = 0
while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))
    contador += 1
    if numero % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1
print("-----------------------------------------")
print(f"Foram {contadorPares} números pares e {contadorImpares} números ímpares")

