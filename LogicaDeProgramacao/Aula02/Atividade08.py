temp = float(input("Insira a temperatura: "))

if temp >= 39.5:
    print("Febre Grave")
elif temp > 38.5 and temp <= 39.4:
    print("Febra Moderada")
elif temp > 37.8 and temp <= 38.5:
    print("Febre Leve")
elif temp > 37 and temp <= 37.8:
    print("Febril")
else:
    print("Temperatura Normal")
