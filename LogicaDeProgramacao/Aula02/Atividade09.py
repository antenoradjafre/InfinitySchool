time1 = input("Insira um time de futebol: ")
golsTime1 = int(input("Insira quantos gols ele fez: "))
time2 = input("Insira outro time de futebol: ")
golsTime2 = int(input("Insirta quantos gols ele fez: "))

if golsTime1 > golsTime2:
    print(time1 + " Ganhou o jogo")
elif golsTime1 < golsTime2:
    print(time2 + " Ganhou o jogo")
else:
    print("Empate")

