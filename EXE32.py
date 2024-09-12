a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))
soma=a+b
print(f"A soma é: {soma}")
if soma > c:
    print(f"e o valor {soma} é maior que o valor de C")
elif soma < c:
    print(f"e o valor {soma} é menor que o valor de C")
else:
    print("e a soma dos valores são iguais ao valor de C")