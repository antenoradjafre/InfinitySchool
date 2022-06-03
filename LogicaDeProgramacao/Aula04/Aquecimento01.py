nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

if len(nome1) > len(nome2):
    print(nome1)
elif len(nome1) < len(nome2):
    print(nome2)
else:
    print("Nomes tem o mesmo tamanho")
