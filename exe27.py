opcao = 1
while opcao==1:
    numero1 = int(input("Digite 1º nota: "))
    num2 = int(input("Digite 2º nota: "))

    while num2 == 0:
        num2 = int(input(" Valor inválido! Digite 2º numero: "))

    divisao = numero1 / num2
    print(divisao)
    opcao = int(input("Deseja continuar: \n"
                      "1 para sim\n"
                      "2 para não: "))
