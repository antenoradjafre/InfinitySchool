'''Insira um numero, verifique se ele é primo'''
while True:
    divisores = 0
    numero = int(input("Digite um número: "))

    for i in range(1, numero+1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print(f"Número {numero} é primo")
    else:
        print(f"Número {numero} não é primo")