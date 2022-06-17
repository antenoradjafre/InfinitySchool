i = 1
media = 0
soma = 0
while i <= 10:
    idade = int(input("Insira uma idade: "))
    soma = soma + idade
    i = i + 1
media = soma/10

print(media)

if media <= 18:
    print("Populaçao Jovem")
elif 18 < media <= 58:
    print("Populacao adulta")
else:
    print("Populacao idosa")
