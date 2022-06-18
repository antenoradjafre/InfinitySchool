def pede_numeros():
    numeros: [int] = []
    for i in range(0, 10):
        numero = int(input("Digite um número: "))
        numeros.insert(i, numero)
    return numeros


def apresenta_pares(numeros):
    pares = []
    for i in range(0, len(numeros)):
        if numeros[i] % 2 == 0:
            pares.append(numeros[i])
    return pares


print(apresenta_pares(pede_numeros()))
