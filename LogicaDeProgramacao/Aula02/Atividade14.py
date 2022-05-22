print("Responda s para sim ou n para não nas perguntas abaixo")
res1 = input("Febre alta ?")
res2 = input("Dores de cabeça ?")
res3 = input("Dores musculares ?")
res4 = input("Manchas vermelhas na pele ?")

sim = 0

if res1 == "s":
    sim += 1

if res2 == "s":
    sim += 1

if res3 == "s":
    sim += 1

if res4 == "s":
    sim += 1

if sim <= 2:
    print("Ficar em repouso e acompanhar evolução dos sintomas")
else:
    print("Paciente com degue procure um médico")
