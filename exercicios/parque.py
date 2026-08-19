print("Para entrar na montanha russa você deve atender os requisitos mínimos")
print("Preencha os dados a seguir: ")
print(" ")

nome = input("Digite o seu nome")
altura = float(input("Qual a sua altura ?: "))
 
if altura >= 1.50:
    print("Acesso liberado! Divirta-se na queda livre!", nome)
elif altura < 1.50:
    print("Desculpe ", nome, "você não tem a altura mínima...")
