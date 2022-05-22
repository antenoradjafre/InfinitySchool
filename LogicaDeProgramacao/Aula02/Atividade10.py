porta1 = "Gorila Grodd"
porta2 = "Bicicleta Caloi"
porta3 = "Leão Proerd"
porta4 = "Fofão"

porta = int(input("Escolha uma das portas de 1 a 4: "))

if porta == 1:
    print(porta1 + " Apareceu")
elif porta == 2:
    print(porta2 + " Apareceu")
elif porta == 3:
    print(porta3 + " Apareceu")
elif porta == 4:
    print(porta4 + " Apareceu")
else:
    print("Número inválido")
