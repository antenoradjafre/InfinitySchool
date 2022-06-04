vogais = 0
consoantes = 0
nome = 'Francisco Antenor Vale Adjafre'
nomeTrimmed = nome.replace(" ", "")
for char in nomeTrimmed.lower():
    if char in ('aeiou'):
        vogais += 1
    else:
        consoantes += 1

print(f"Existem {vogais} vogais e {consoantes} consoantes")
