def pede_numeros():
    numeros: [int] = []
    for i in range(0, 5):
        numero = int(input("Digite um número: "))
        numeros.insert(i, numero)
    return numeros


def calcula_quadrados(numeros):
    quadrados: [int] = []
    for i in range(0, len(numeros)):
        quadrados.insert(i, numeros[i] ** 2)
    return quadrados


numeros = pede_numeros()
print(numeros)
print(calcula_quadrados(numeros))
