def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def caos(num1, num2):
    print(f'Resultado da soma é: {soma(num1, num2)}')
    print(f'Resultado da subtração é: {sub(num1, num2)}')
    print(f'Resultado da multiplicação é: {mult(num1, num2)}')
    print(f'Resultado da divisão é: {div(num1, num2)}')

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))
caos(numero1, numero2)
