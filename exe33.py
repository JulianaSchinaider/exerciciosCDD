opcao = 1
while opcao ==1:
    x=float(input("Digite um número: "))
    if x>0:
        print("Valor positivo")
    elif x<0:
        print("Valor negativo")
    else:
        print("Valor igual a zero")
    if x%2==0:
        print("Valor é par")
    else:
        print("o número é ímpar")
    opcao = int(input("Deseja continuar: \n"
                  "1 para sim\n"
                  "2 para não"))

#---------------------------------------#
# if x%2==0:
#if numero > 0:
#       print("número par positivo")
#   else:
#       print("número par negativo")
#else:
# if numero <0:
#       print("número impar negativo")
#   else:
#       print:("número impar positivo")
# para acrescentar a lógica do WHILE precisa colocar A VARIAVEL OPCAO
# antes e no final DENTRO do while
#----------------------------------------#
