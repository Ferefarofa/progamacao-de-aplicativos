def aplicar_promocao(lista):
    lista_nova = []
    for item in lista:
        if item >= 100.0:
            desconto = item * 0.15
            item -= desconto
            lista_nova.append(item)
        else:
            lista_nova.append(item)
    print(lista_nova)
lista = lista_compras = [150.0, 80.0, 200.0, 50.0]
aplicar_promocao(lista)
        