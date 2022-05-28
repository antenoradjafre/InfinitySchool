escolhido = 7
while True:
    numero = int(input("Insira um número entre 1 e 10: "))
    if numero > escolhido:
        print("Número é maior que o escolhido")
    elif numero < escolhido:
        print("Número é menor que o escolhido")
    elif numero == escolhido:
        print("Acertou Mizeravi!!!!!!!")
