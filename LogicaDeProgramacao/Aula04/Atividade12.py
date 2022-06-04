preco = float(input("Digite o valor do preço do pão: "))
for i in range(1, 51):
    print(f'{i} - Preço: R${(preco * (i)):.2f}')
