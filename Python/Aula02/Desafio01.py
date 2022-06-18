def conta_vogal(texto, vogal):
    qtd_vogal = 0
    texto_trimmado = texto.replace(" ", "")
    for char in texto_trimmado.lower():
        if char in (vogal):
            qtd_vogal += 1
    return qtd_vogal


def pede_texto():
    texto = input("Escreva um texto: ")
    return texto


texto = pede_texto()
dict = {
    "A": conta_vogal(texto, "a"),
    "E": conta_vogal(texto, "e"),
    "I": conta_vogal(texto, "i"),
    "O": conta_vogal(texto, "o"),
    "U": conta_vogal(texto, "u"),
}

print(dict)
