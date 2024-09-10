hora1 = int(input("digite hora 1: "))
hora2 = int(input("digite hora 2: "))
minutos1= int(input("Digite minutos 1: "))
minutos2=int(input("Digite minutos 2: "))

soma1=hora1+hora2
print(soma1)
soma2=minutos1+minutos2
print(soma2)

if soma1 > 12:
   soma1 = soma1 -12

if soma2 > 12:
   soma2 = soma2 -12

somah = horas1 + horas2
somam = minutos2 + minutos2

if somam >=60:
    somam=somam - 60
    somah=somah + 1

if somah >= 12:
    somah = somah - 12

if somah >12:
    somah-=12

print(f"{somah},{somam:02d}")







