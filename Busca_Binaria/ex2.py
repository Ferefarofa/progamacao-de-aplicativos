vetor = [3, 8, 1, 1, 1, 7, 2, 6, 4, 10]
numero = int(input("Digite o número: "))
sequencia = 0
for valor in vetor:
    if valor == numero:
        sequencia += 1
        
print(f"O numero se repete {sequencia} vezes")
    