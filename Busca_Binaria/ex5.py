vetor = [3, 8, 1, 9, 1, 7, 2, 1, 4, 3]
numero = int(input("Digite o número: "))
indice0 = 0
indicef = 0
indiceref = 0
for valor in vetor:
    if valor == numero:
        break
    indice0 += 1
for valor in vetor:
    indiceref +=1
    if valor == numero:
        indicef = indiceref - 1

print(f"Indice inicial é {indice0}, e o indice final é {indicef}.")
