'''Dado um intervalo diga quais os numeros primos entre eles'''
quantidade = 0
sup = int(input("Digite o intervalo superior: "))

for i in range(0, sup+1):
    divisores = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisores += 1

    if divisores == 2:
        print(f"{i}")
        quantidade += 1

print(f"Existem {quantidade} números primos de 0 a {sup}")
