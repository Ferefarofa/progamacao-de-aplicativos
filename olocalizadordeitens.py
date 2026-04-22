ferramentas = ["Martelo", "Chave de fenda", "Furadeira", "Alicate"]
frutas = ["Banana", "Manga", "Melão", "Melancia"]
def esta_na_lista(nome, lista):
    while nome != "Terminar":
        if nome in lista:
            print(f"{nome} está em {lista}")
        elif nome not in lista:
            print(f"{nome} não está em {lista}")
nome = input("Digite o nome: ")
esta_na_lista(nome, lista)
