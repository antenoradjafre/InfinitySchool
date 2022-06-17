def qtdChar(frase):
    qtd = 0
    fraseTrimmed = frase.replace(" ", "")
    return len(fraseTrimmed)

frase = input('Digite uma frase: ')
print(f'Quantidade de caracteres na frase é: {qtdChar(frase)}')
