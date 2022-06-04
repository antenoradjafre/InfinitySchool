qtd_pares = 0
qtd_impares = 0
for i in range(0, 10):
    num = int(input("Insira um número inteiro e positivo: "))

    if num % 2 == 0:
        qtd_pares += num
    else:
        qtd_impares += num

print(f"Soma dos números pares é: {qtd_pares} e de ímpares é: {qtd_impares}")
