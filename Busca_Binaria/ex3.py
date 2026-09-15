vetor = [3, 8, 1, 9, 5, 7, 2, 6, 4, 10]
referencia = 0
for valor in vetor:
    if valor > referencia:
        referencia = valor
print("O maior número é", referencia)
indice = 0
for valor in vetor:
    if valor == referencia:
        print("E esta no índice:", indice)
        break
    indice += 1