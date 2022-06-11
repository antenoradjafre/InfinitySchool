def qtdInteiros(num1):
    soma = 0
    i = 0
    while i < num1:
        i = i + 1
        soma = soma + i
        print(soma)



num = int(input('Digite um numero inteiro positivo: '))
qtdInteiros(num)