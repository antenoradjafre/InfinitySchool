nota = 0
qtd = 0

while True:
    nota += float(input('Digite uma nota: '))
    continua = input('Digite 00 para parar ou Enter para inserir uma nova nota: ')
    qtd += 1
    if continua == '00':
        break

print(f'A média é: {(nota/qtd):.2f}')

