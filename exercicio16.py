numero = int(input("Digite um numero: "))

for x in range(1,numero,1):
    if (x %2 !=0):
        print(f"{x}", end= " ")
