def lista_de_inteiros():
    numeros: [int] = []
    for i in range(0, 10):
        numero = int(input("Digite um numero: "))
        numeros.insert(i, numero)
    return numeros


def copia_valores_lista(numeros):
    lista_a_remover: [int] = []
    for i in range(0, len(numeros)):
        lista_a_remover.insert(i, numeros[i])
    return lista_a_remover


def remover_numeros_pares(numeros):
    lista_a_remover: [int] = copia_valores_lista(numeros)
    for numero in numeros:
        if numero % 2 == 0:
            lista_a_remover.remove(numero)
    return lista_a_remover


numeros = lista_de_inteiros()
print(remover_numeros_pares(numeros))
