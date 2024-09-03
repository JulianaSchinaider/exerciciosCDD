time1=input("Digite nome do 1º time: ")
gols1=int(input(f"Digite quant. de gols o {time1}: "))

time2=input("Digite nome do 2º time: ")
gols2=int(input(f"Digite quant. de gols o {time2}: "))

if gols1 > gols2:
    print(f"{time1} é o vencedor")

elif gols1 < gols2:
       print(f"{time2} é o vencedor")
else:
    print("EMPATE")


