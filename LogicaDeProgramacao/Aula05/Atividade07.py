def aritimetica(num1, num2, operacao):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtração':
        return num1 - num2
    elif operacao == 'multiplicação':
        return num1 * num2
    elif operacao == 'divisão':
        return num1 / num2
    else:
        print(f'Operação inválida, assumindo soma')
        return num1 + num2


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operacao = input('Digite a operação: ')
resultado = aritimetica(num1, num2, operacao)
print(f'Resultado da {operacao} é {resultado:.2f}')

