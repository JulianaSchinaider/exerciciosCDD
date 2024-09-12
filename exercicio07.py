n1 = float(input("Digite o 1º nota: "))
n2 = float(input("Digite o 2º nota: "))
n3 = float(input("Digite o 3º nota: "))
media = ((n1+n2+n3)/3, "media")
print(media)

if media >= 7:
    print("Aprovado")
else:
    if media >=4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")

