aluno = int(input("Digite quant. de alunos existentes: "))
somanota=0
for x in range(aluno):
    nota = float(input("Digite a nota do aluno: "))
    somanota = nota+somanota

media= somanota/aluno

print(media)
