pessoas = {}
for i in range(0, 2):
    nome = input('Digite o nome de uma pessoa: ')
    cpf = input("Digite o CPF: ")
    if cpf in pessoas:
        print("Valor CPF já existente")
    else:
        pessoas[cpf] = nome


print(f'Pessoas: {pessoas}')
