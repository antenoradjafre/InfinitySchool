def verificaNumeros(num1, num2):
    #Quantidade de pares que mostrará ao final do programa
    qtdpares = 0
    #Mod 2 para dizer se é par ou impar
    if num1 % 2 == 0:
        #Soma 1 na quantidade de pares caso o primeiro numero seja par
        qtdpares = qtdpares + 1
    if num2 % 2 == 0:
        # Soma 1 na quantidade de pares caso o segundo numero seja par
        qtdpares = qtdpares + 1
    return qtdpares


numero1 = int(input("Insira numero 1: "))
numero2 = int(input("Insira numero 2: "))

#Return vai retornar a quantidade de numeros pares para a variável quantidade que irá mostrar esse numero no print
quantidade = verificaNumeros(numero1, numero1)
print(f'Há {quantidade} de números pares')
