alunos = ("amanda", "vinicius", "carlos")
notas = (40, 60, 70)
aprovados = []
if notas[0] >= 60:
    aprovados.append(alunos[0])
if notas[1] >= 60:
    aprovados.append(alunos[1])
if notas[2] >= 60:
    aprovados.append(alunos[2])
print(f"Alunos aprovados são: {aprovados}")