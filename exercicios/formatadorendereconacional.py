def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    print(f"RUA: {rua}, NÚMERO: {numero}, BAIRRO: {bairro}, CIDADE: {cidade}, CEP: {cep}.")
rua_end = input("Nome da rua do endereço: ")
numero_end = input("Número do endereço: ")
bairro_end = input("Bairro do endereço: ")
cidade_end = input("Cidade do endereço: ")
cep_end = input("CEP do endereço: ")
gerar_etiqueta(rua_end, numero_end, bairro_end, cidade_end, cep_end)
