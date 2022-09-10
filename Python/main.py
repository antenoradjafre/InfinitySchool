from PyQt5 import uic, QtWidgets
import mysql.connector


banco = mysql.connector.connect(
    user='user',
    database='funcionario',
    passwd='password',
    port='3306'
)


def cadastrarUsuario():
    cadastroUsuarioView.show()
    cadastroUsuarioView.pushButton.clicked.connect(salvarUsuario)
    cadastroUsuarioView.pushButton_2.clicked.connect(exibirUsuario)


def salvarUsuario():
    linhaUm = cadastroUsuarioView.lineEdit.text()
    linhaDois = cadastroUsuarioView.lineEdit_2.text()
    cursor = banco.cursor()
    comandoSql = f'insert into usuario (nome, senha) values(%s, %s)'
    dados = (str(linhaUm), str(linhaDois))
    cursor.execute(comandoSql, dados)
    banco.commit()


def exibirUsuario():
    exibirUsuarioView.show()
    cursor = banco.cursor()
    comandoSql = f'select * from usuario'
    cursor.execute(comandoSql)
    dados_lidos = cursor.fetchall()

    exibirUsuarioView.tableWidget.setRowCount(len(dados_lidos))
    exibirUsuarioView.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0,3):
            exibirUsuarioView.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


def cadastrarProduto():
    cadastroProdutoView.show()
    cadastroProdutoView.pushButton.clicked.connect(salvarProduto)


def salvarProduto():
    produto = cadastroProdutoView.lineEdit.text()
    qtd = cadastroProdutoView.lineEdit_2.text()
    descricao = cadastroProdutoView.lineEdit_3.text()
    preco = cadastroProdutoView.lineEdit_4.text()


    cursor = banco.cursor()
    comandoSql = f'insert into produto (chave, descricao, qtd, preco) values(%s, %s, %s, %s)'
    dados = (str(produto), str(descricao), int(qtd), float(preco))
    cursor.execute(comandoSql, dados)
    banco.commit()

    cadastroProdutoView.show()


#Inicio
#Gerando a aplicacao
app = QtWidgets.QApplication([])

#Carregar o Arquivo .ui
telaInicial = uic.loadUi('View/TelaInicial.ui')
cadastroUsuarioView = uic.loadUi('View/CadastroUsuario.ui')
cadastroProdutoView = uic.loadUi('View/CadastroProduto.ui')
exibirUsuarioView = uic.loadUi('View/ExibirUsuario.ui')
telaInicial.pushButton.clicked.connect(cadastrarUsuario)
telaInicial.pushButton_2.clicked.connect(cadastrarProduto)

#Exibir Minha Tela
telaInicial.show()
app.exec()
