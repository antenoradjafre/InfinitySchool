numero1 = int(input("Digite um numero inteiro e positivo: "))
numero2 = int(input("Digite outro numero inteiro e positivo: "))

opcao = int(input("Digite: \n 1 - para somar \n 2 - para subtrair \n 3 - para multiplicar \n 4 - para dividir \n "))

if opcao == 1:
    print("Resultado é: ", numero1 + numero2)
elif opcao == 2:
    print("Resultado é: ", numero1 - numero2)
elif opcao == 3:
    print("Resultado é: ", numero1 * numero2)
elif opcao == 4:
    print("Resultado é: ", numero1 / numero2)
else:
    print("Opção Invalida")

