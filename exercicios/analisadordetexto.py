def contar_caracteres(palavra):
    if len(palavra) < 5:
        print("Nome muito curto, mínimo de 5 caracteres")
    else:
        print("Nome cadastrado com sucesso! ")
nome = input("Digite o seu nome de registro: ")
contar_caracteres(nome)