# Aquecimento 01
#
# Determinada empresa resolveu dar um aumento a todos seus funcionários seguindo a seguinte tabela:
# - Salários até R$1.000,00 – ajuste de 15%
# - Salários até R$3.000,00 – ajuste de 10%
# - Salários acima de R$3.000,00 – ajuste de 5%
#
# Crie um algoritmo que solicite o salário e, em seguida, informe o valor reajustado.

ajuste15 = 1.15
ajuste10 = 1.10
ajuste5 = 1.05

salario = float(input("Insira o salario: "))

if salario <= 1000:
    salario = salario * ajuste15
elif 1000 < salario <= 3000:
    salario = salario * ajuste10
elif salario > 3000:
    salario = salario * ajuste5

print(salario)
