def calculaSeculo(ano):
    if ano % 100 == 0:
        funSeculo = int(ano / 100)
    else:
        funSeculo = int(ano / 100 + 1)
    return funSeculo


def intParaRoman(num):
    valor = ''
    cont = 0
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    while num > 0:
        for i in range(num // numeros[cont]):
            valor += romanos[cont]
            num -= numeros[cont]
        cont += 1
    return valor


ano = int(input("Digite um ano: "))
seculo = calculaSeculo(ano)
seculoRomano = intParaRoman(seculo)
print(f'O século é: {seculoRomano}')


