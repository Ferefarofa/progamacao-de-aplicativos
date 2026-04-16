lista = []
listadobrados = []
adicionar = ""
while adicionar != 0:
    adicionar = int(input("Digite números para dobrá-los(Para finalizar digite 0): "))
    if adicionar != 0:
        lista.append(adicionar)
        print(f"Número {adicionar} adicionado. ")
print("Lista anterior: ", lista)
for item in lista:
    print(f"Número {item} dobrado. ")
    item = item * 2
    listadobrados.append(item)
print("Os numero dobrados são respectivamente: ", listadobrados)