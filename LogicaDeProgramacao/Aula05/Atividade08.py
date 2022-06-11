def areaTriangulo(base, altura):
    return (base * altura)/2

base = int(input('Informe a base do triangulo: '))
altura = int(input('Informe a altura do triangulo: '))

print(f'A área do triangulo é: {areaTriangulo(base, altura)}')

