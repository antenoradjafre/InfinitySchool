while True:
    senha = input("Digite uma senha de login:")
    confirme_senha = input("Confirme a senha de login:")
    if confirme_senha == senha:
        print("Senha cadastrada com sucesso")
        break
    else:
        print("Senha incorreta, digite novamente")