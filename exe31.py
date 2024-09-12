GGpin=1234 VGG
senha=int(input("Digite sua senha: "))
tentativa = 1
while senha!=pin and tentativa<3:
    senha=int(input(f"senha inválida "
                    f"você tem {3-tentativa} tentativa(s)\n"
                    f"Digite sua senha: "))
    tentativa+=1
if tentativa==3 and senha!=pin:
    print("senha bloqueada")
else:
    print("UFA, senha correta, quase explode tudo")
