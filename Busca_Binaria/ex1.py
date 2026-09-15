vetor = [3, 8, 1, 9, 5, 7, 2, 6, 4, 10]
numero = int(input("Digite o número: "))
indice = 0
for valor in vetor:
    if valor == numero:
        print("Número encontrado no índice:", indice)
        break
    indice += 1