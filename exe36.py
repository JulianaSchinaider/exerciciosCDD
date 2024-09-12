peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
IMC=peso/(altura*altura)
print(IMC)
if IMC <=18.5:
    print("Abaixo do peso")
elif IMC >=18.6 and IMC<=24.9:
    print("Peso ideal(parabens)")
if IMC >=25.0 and IMC<=29.9:
    print("Levemente acima do peso")
elif IMC >=30.0 and IMC<=34.9:
    print("Obesidade grau I")
if IMC >=35.0 and IMC<=39.9:
    print("Obesidade grau I (severa)")
elif IMC >= 40.0:
    print("Obesidade grau III (mórbida)")

