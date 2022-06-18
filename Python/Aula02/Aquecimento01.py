from datetime import date

def calculaIdade(ano, mes, dia):
    dia_de_hoje = int(date.today().day)
    mes_de_hoje = int(date.today().month)
    ano_de_hoje = int(date.today().year)
    idade = ano_de_hoje - ano

    if mes > mes_de_hoje:
        idade -= 1
    elif mes == mes_de_hoje:
        if dia < dia_de_hoje:
            idade -= 1

    return idade


ano = int(input("Digite seu ano de nascimento em yyyy: "))
mes = int(input("Digite o seu mes de nascimento em mm: "))
dia = int(input("Digite seu dia de nascimento em dd: "))
print(calculaIdade(ano, mes, dia))




