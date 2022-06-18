pessoas = []
idades = []
for i in range(0, 5):
    nome = input('Digite o nome de uma pessoa: ')
    idade = input("Digite a idade: ")
    pessoas.insert(i, nome)
    idades.insert(i, idade)

print(pessoas)
print(idades)

