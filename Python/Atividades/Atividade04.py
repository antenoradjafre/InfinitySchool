from PySimpleGUI import PySimpleGUI as infinity

#Layout
infinity.theme("Reddit")
colunas_e_linhas = [
    [infinity.Text("Login do Usuário"), infinity.Input(key='login_do_usuario')],
    [infinity.Text("Senha"), infinity.Input(key='senha', password_char='*')],
    [infinity.Checkbox('Salvar Senha')],
    [infinity.Button('Entrar'), infinity.Button('Sair')]
]

#Janela
janela = infinity.Window('Tela de Login', colunas_e_linhas)

#Back - Eventos
while True:
    evento, valores = janela.read()
    if evento == 'Sair':
        break
    if evento == 'Entrar':
        if valores['login_do_usuario'] == 'Antenor' and valores['senha'] == '123456':
            print('Bem vindo !!!')


janela.close()