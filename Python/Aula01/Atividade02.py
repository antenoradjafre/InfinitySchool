def contadorDeVogais(nome):
    vogais = 0
    consoantes = 0
    nomeTrimmed = nome.replace(" ", "")
    for char in nomeTrimmed.lower():
        if char in ('aeiou'):
            vogais += 1
        else:
            consoantes += 1

    print(f"Existem {vogais} vogais e {consoantes} consoantes em {nome}")


nome = input("Informe seu nome completo: ")
contadorDeVogais(nome)
