def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valor_imposto = valor_base + (valor_base* (imposto_percentual / 100))
    if cupom_desconto > valor_imposto:
        valor_final = 0
    else:
        valor_final = valor_imposto - cupom_desconto
    print(f"O valor final a pagar é {valor_final}")
valor_produto = float(input("Qual o valor do produto ?: "))
imposto = float(input("Qual do valor do imposto em '%' ?: "))
desconto = float(input("Qual o valor do cupom de desconto ?: "))
calcular_preco_final(valor_produto, imposto, desconto)