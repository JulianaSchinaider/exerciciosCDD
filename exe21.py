aluno = int(input("Digite quantidade de alunos: "))
n=0
soma = 0
while n < aluno:
    num = int(input("digite um número"))
    soma = soma + num
    media = soma / aluno
    print(n)
    n = n + 1
    print(f"A média total é: {media}")