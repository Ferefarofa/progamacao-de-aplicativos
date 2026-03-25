cidades = ["batataazul", "São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
perg = input("\nDigite o nome de uma cidade para descobrir a sua posição: ")
if perg in cidades:
    print(f"\nA cidade inserida está na posição: {cidades.index(perg)}")
else:
    print("Cidade não localizada. ")
    