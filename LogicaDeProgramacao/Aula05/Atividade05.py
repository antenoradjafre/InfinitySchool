def maiorDosPares():
    numero1 = int(input("Digite um número par: "))
    numero2 = int(input("Digite outro número par: "))

    if numero1 % 2 == 0 and numero2 % 2 == 0:
        if numero1 > numero2:
            return numero1
        else:
            return numero2
    else:
        print("Valores pares digitados incorretamente, assumindo 0 como valor")
        return 0


def maiorDosImpares():
    numero1 = int(input("Digite um número ímpar: "))
    numero2 = int(input("Digite outro número ímpar: "))

    if numero1 % 2 != 0 and numero2 % 2 != 0:
        if numero1 > numero2:
            return numero1
        else:
            return numero2
    else:
        print("Valores ímpares digitados incorretamente, assumindo 0 como valor")
        return 0


soma = maiorDosPares() + maiorDosImpares()
print(f'Soma dos valores é {soma}')