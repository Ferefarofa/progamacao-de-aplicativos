vagas = ["Livre", "Ocupado", "Livre", "Ocupado"]
escolha = int(input("Escolha uma vaga de 0 a 3: "))
if escolha  % 2 == 0 and vagas[escolha] == "Livre":
    print(f"Vaga {escolha}")
else:
    print("Indisponivel ou fora das regras.")