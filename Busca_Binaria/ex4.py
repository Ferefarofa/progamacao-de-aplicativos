vetor = ['lala', 'lele', 'lili', 'lolo', 'lulu']
nome = input("Digite o nome: ")

for valor in vetor:
    if valor == nome:
        resultado =  "Nome encontrado."
        break
    else:
        resultado = "Nome não encontrado."
print(resultado)
