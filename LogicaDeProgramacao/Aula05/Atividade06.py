def mensagem(nome, msg = 'Boa aula, '):
    if nome == '':
        print(f'{msg}Fulaninho de Tal.')
    else:
        print(f'{msg}{nome}.')

nome = input('Escreva um nome: ')
mensagem(nome)

