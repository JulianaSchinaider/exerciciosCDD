opcao = 1
while opcao==1:
    numero1 = int(input("Digite 1º numero: "))
    num2 = int(input("Digite 2º numero: "))
<<<<<<< HEAD
    while num2 == 0:
        num2 = int(input(" Valor inválido! Digite 2º numero: "))
=======

    while num2 == 0:
        num2 = int(input(" Valor inválido! Digite 2º numero: "))

>>>>>>> 6e1edc0cd7a6da83917246fb89c0dde5faae700a
    divisao = numero1 / num2
    print(divisao)
    opcao = int(input("Deseja continuar: \n"
                      "1 para sim\n"
                      "2 para não: "))
