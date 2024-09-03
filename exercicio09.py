combustivel=input("Qual o tipo de combustível: ")
quantlitros=float(input("Digite quantos litros de combustivel: "))
preco1=5.80
preco2=4.90

if combustivel=="G":
    print(preco1*quantlitros)
elif combustivel=="E":
    print(preco2*quantlitros)

