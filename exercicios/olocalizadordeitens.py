ferramentas = ["Martelo", "Chave de fenda", "Furadeira", "Alicate"]
frutas = ["Banana", "Manga", "Melão", "Melancia"]
def esta_na_lista(nome, lista):
        if nome in lista:
            print(f"{nome} está em {lista}")
        elif nome not in lista:
            print(f"{nome} não está em {lista}")
nome = input("Digite o nome: ")
lista = input("Digite a lista: ")
if lista == "ferramentas":
    esta_na_lista(nome, ferramentas)
elif lista == "frutas":
    esta_na_lista(nome, frutas)

