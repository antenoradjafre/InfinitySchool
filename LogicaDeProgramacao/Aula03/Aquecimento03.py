usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")


if usuario.lower() == "admin" and senha == "619":
    print("Acesso liberado")
else:
    print("Acesso bloqueado")
