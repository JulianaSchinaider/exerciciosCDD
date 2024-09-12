opcao = 0
while opcao==0:
    nota1 = int(input("Digite 1ª nota: "))
    while nota1>10 or nota1<0:
        print("nota invalida: ")
        nota1=float(input("Digite uma nota de 0 a 10: "))

    nota2=float(input("Digite 2ª nota: "))

    while nota2>10 or nota2<0:
        print("nota invalida: ")
        nota2=float(input("Digite uma nota de 0 a 10: "))

    print(f"As notas são:\n"
      f"[-----{nota1} e {nota2}-----]")

    media=(nota1+nota2)/2
    print(f"a media do aluno: {media} ")

    while opcao==1:
        opcao = int(input("Deseja realizar novo cálculo? \n"
                      "0 para sim\n"
                      "1 para não: "))
    opcao=int(input("0 para continuar 1 para finalizar"))