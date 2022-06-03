capitalInvestido = float(input("Insira o capital investido: "))
juros = float(input("Insira a taxa de juros: "))
juros = juros/100
modalidade = int(input("Digite 1 para juros simples ou 2 para juros composto: "))
tempo = int(input("Digite o tempo em meses: "))
montante = 0

if modalidade == 1:
    montante = capitalInvestido * (1 + juros * tempo)
    print(f"Montante será de: {montante}")
elif modalidade == 2:
    montante = capitalInvestido * (1 + juros ) ** tempo
    print(f"Montante será de: {montante} reais")
else:
    print("Modalidade inválida")
