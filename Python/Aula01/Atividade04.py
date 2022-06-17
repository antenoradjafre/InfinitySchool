def somaPercent(num1, num2):
    porcentagem = num2/100
    aumento = num1*porcentagem + num1
    return aumento

numero1 = int(input("Digite um número inteiro: "))
porcentagem = float(input("Digite uma porcentagem: "))
valor = somaPercent(numero1, porcentagem)
print(f"O valor com aumento é: {valor}")