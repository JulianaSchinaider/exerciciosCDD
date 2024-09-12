n=1
soma = 0
while n<=10:
  print(f"estamos no passo {n} e a soma é {soma}")
  num = int(input("digite um número"))
  soma = soma + num
  media = soma / num
  print(n)
  n = n + 1
print(f"A média é: {media}")