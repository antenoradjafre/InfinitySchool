while True:
    numero = int(input("Digite um valor entre 0 e 10: "))
    if numero >= 0 and numero <= 10:
        print("Número correto")
        break
    else:
        print("Número inválido, tente novamente")
