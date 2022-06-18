def cadastro():
    ano = {
        "Janeiro": 0.0,
        "Fevereiro": 0.0,
        "Março": 0.0,
        "Abril": 0.0,
        "Maio": 0.0,
        "Junho": 0.0,
        "Julho": 0.0,
        "Agosto": 0.0,
        "Setembro": 0.0,
        "Outubro": 0.0,
        "Novembro": 0.0,
        "Dezembro": 0.0
    }
    for mes in ano:
        temperatura = float(input(f"Insira a temperatura média do mês {mes}: "))
        ano[mes] = temperatura
    return ano


def calcula_media_anual(ano):
    soma = 0
    for temperatura in ano.values():
        soma += temperatura
    mediaTemperatura = soma/len(ano.values())
    return mediaTemperatura


def meses_acima_da_media(ano, media_anual):
    meses_acima = []
    for mes, temperatura in ano.items():
        if temperatura >= media_anual:
            meses_acima.append(mes)
    return meses_acima


ano = cadastro()
media_anual = calcula_media_anual(ano)
print(meses_acima_da_media(ano, media_anual))
