def calculaSeculo(ano):
    if ano % 100 == 0:
        funSeculo = int(ano / 100)
    else:
        funSeculo = int(ano / 100 + 1)
    return funSeculo

ano = int(input("Digite um ano: "))
seculo = calculaSeculo(ano)
print(f'O século é: {seculo}')

