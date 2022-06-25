nomes = []
cpfs = []
for i in range(0, 5):
    nome = input('Digite o nome de uma pessoa: ')
    cpf = input("Digite o CPF: ")
    if cpf in cpfs:
        print("Valor CPF já existente")
    else:
        nomes.insert(i, nome)
        cpfs.insert(i, cpf)

print(f'Nomes: {nomes} --- CPF: {cpfs}')



