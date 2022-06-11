def verificaNumer(num):
    if num < 0:
        print("numero negativo")
    elif num > 0 :
        print("numero positivo")
    else:
        print("nulo")

numero = int(input("Insira um numer: "))
verificaNumer(numero)

