qtd_pares = 0
inicio = int(input("Digite um número para ser o limite inferior: "))
fim = int(input("Digite um número para ser o limite superior: "))
for i in range(inicio, fim):

    if i % 2 == 0:
        qtd_pares += 1

print(f"Quantidade de números pares é: {qtd_pares} ")
