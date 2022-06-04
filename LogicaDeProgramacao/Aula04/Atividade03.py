soma = 0
qtd = 0
for i in range(0, 5):
    numero = int(input("Digite um número: "))
    soma = soma + numero
    qtd = qtd + 1

media = (soma/qtd)
print(f"A soma é: {soma} e a média é: {media:.2f}")
