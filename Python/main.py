from PyQt5 import uic, QtWidgets
import mysql.connector


banco = mysql.connector.connect(
    user='user',
    database='funcionario',
    passwd='password',
    port='3306'
)

def cadastroUsuario():
    cadastroUsuarioView.show()
    linhaUm = cadastroUsuarioView.lineEdit.text()
    linhaDois = cadastroUsuarioView.lineEdit_2.text()

    cursor = banco.cursor()
    comandoSql = f'insert into usuario (nome, senha) values(%s, %s)'
    dados = (str(linhaUm), str(linhaDois))
    cursor.execute(comandoSql, dados)
    banco.commit()

def cadastroProduto():
    cadastroProdutoView.show()
    produto = cadastroProdutoView.lineEdit.text()
    qtd = cadastroProdutoView.lineEdit_2.
    descricao = cadastroProdutoView.lineEdit_3.text()
    preco = cadastroProdutoView.lineEdit_4.text()


    cursor = banco.cursor()
    comandoSql = f'insert into produto (chave, descricao, qtd, preco) values(%s, %s, %s, %s)'
    dados = (str(produto), str(descricao), int(qtd), float(preco))
    cursor.execute(comandoSql, dados)
    banco.commit()




#Inicio
#Gerando a aplicacao
app = QtWidgets.QApplication([])

#Carregar o Arquivo .ui
telaInicial = uic.loadUi('TelaInicial.ui')
cadastroUsuarioView = uic.loadUi('CadastroUsuario.ui')
cadastroProdutoView = uic.loadUi('CadastroProduto.ui')
telaInicial.pushButton.clicked.connect(cadastroUsuario)
telaInicial.pushButton_2.clicked.connect(cadastroProduto)

#Exibir Minha Tela
telaInicial.show()
app.exec()
