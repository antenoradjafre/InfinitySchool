def piramide(num):
    for i in range(1, num+1):
        for j in range(i, 1, -1):
            print(i, end=" ")
        print(i)

numero = int(input('Digite um número: '))
piramide(numero)