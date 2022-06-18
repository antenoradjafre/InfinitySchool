def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = input("Digite seu cpf: ")
    endereco = input("Digite seu endereço: ")
    pessoas = {"Nome": nome, "Idade": idade, "CPF": cpf, "Endereço": endereco}
    return pessoas

print(cadastro())


