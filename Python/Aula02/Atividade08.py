def cadastro():
    pessoas = {
        "Antenor": 1.81,
        "Israel": 1.74,
        "Patricia": 1.62,
        "Antonio": 1.44,
        "Claudio": 1.85,
        "Rafael": 1.75,
        "Roberto": 1.47,
        "Laisa": 1.92,
        "Priscila": 1.44,
        "Laura": 1.91
    }
    return pessoas


def filtrando_cadastros(pessoas):
    maiores = []
    for key, value in pessoas.items():
        if value > 1.8:
            maiores.append(key)
    return maiores



print(filtrando_cadastros(cadastro()))