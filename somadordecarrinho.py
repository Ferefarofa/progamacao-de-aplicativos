lista_compras = []
continuar = "S"
def somar_carrinho(lista):
    valor_final = 0
    for item in lista:
        valor_final += item
    if valor_final > 500:
        desconto = valor_final * 0.1
        valor_final -= desconto
        print("Parabéns, sua compra ultrapassou os R$:500,00, você conseguiu um desconto de 10%!!!")
        print(f"O desconto é de R$:{desconto}")
    return(valor_final)
while continuar == "S":
    preco = float(input("Qual o preço do item a adicionar no carrinho de compras ?: "))
    lista_compras.append(preco)
    continuar = input("Deseja adicionar mais algum item ?(S/N): ")
valor_final = somar_carrinho(lista_compras)
print(f"O valor total a pagar é {valor_final}")