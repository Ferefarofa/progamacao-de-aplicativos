vendas = []
def analisar_vendas(nome, lista_vendas, meta_mensal,):
    media_vendas = 0
    for item in lista_vendas:
        media_vendas += item
    media_vendas /= len(lista_vendas)
    if media_vendas >= meta_mensal:
        print(f"O vendedor {nome} teve média de {media_vendas} e bateu a meta! ")
    else:
        print(f"O vendedor {nome} teve média de {media_vendas} e não bateu a meta! ")
nome_vendedor = input("Qual o nome do vendedor ?: ")
meta_do_mes = float(input("Qual a meta mensal media de vendas ?: "))
mais = "S"
while mais == "S":
    vendas_adicionar = float(input("Qual o valor das vendas do mês ?: "))
    vendas.append(vendas_adicionar)
    mais = input("Tem mais valores ?(S/N): ")
analisar_vendas(nome_vendedor, vendas, meta_do_mes)
