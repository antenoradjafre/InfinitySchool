dia = int(input("Insira o dia, em dd, do seu aniversário: "))
mes = input("Escreva o mes do seu aniversário: ")

if mes.upper() == "JANEIRO":
    if dia <= 20:
        print("CAPRICÓRNIO")
    elif dia >= 21:
        print("AQUARIO")

if mes.upper() == "FEVEREIRO":
    if dia <= 18:
        print("AQUARIO")
    elif dia >= 19:
        print("PEIXES")

if mes.upper() == "MARÇO":
    if dia <= 20:
        print("PEIXES")
    elif dia >= 21:
        print("ARIES")

if mes.upper() == "ABRIL":
    if dia <= 20:
        print("ARIES")
    elif dia >= 21:
        print("TOURO")

if mes.upper() == "MAIO":
    if dia <= 20:
        print("TOURO")
    elif dia >= 21:
        print("GEMEOS")

if mes.upper() == "JUNHO":
    if dia <= 20:
        print("GEMEOS")
    elif dia >= 21:
        print("CÂNCER")

if mes.upper() == "JULHO":
    if dia <= 22:
        print("CÂNCER")
    elif dia >= 23:
        print("LEÃO")

if mes.upper() == "AGOSTO":
    if dia <= 22:
        print("LEÃO")
    elif dia >= 23:
        print("VIRGEM")

if mes.upper() == "SETEMBRO":
    if dia <= 22:
        print("VIRGEM")
    elif dia >= 23:
        print("LIBRA")

if mes.upper() == "OUTUBRO":
    if dia <= 22:
        print("LIBRA")
    elif dia >= 23:
        print("ESCORPIÃO")

if mes.upper() == "NOVEMBRO":
    if dia <= 21:
        print("ESCORPIÃO")
    elif dia >= 22:
        print("SAGITÁRIO")

if mes.upper() == "DEZEMBRO":
    if dia <= 21:
        print("SAGITÁRIO")
    elif dia >= 22:
        print("CAPRICÓRNIO")
