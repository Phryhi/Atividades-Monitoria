aprovado = 0
alunos_nota = 0

for i in range(1, 21):
  nota = float(input("Nota: "))
  alunos_nota += nota

  if nota >= 7:
    aprovado += 1

media_turma = alunos_nota / 20
print("alunos aprovados: ", aprovado)
print("media turma: ", media_turma)
