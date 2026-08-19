lista_vip = []
triagem = []
perg = ""
while perg != "fim":
    perg = input("Digite um nome para a lista de convidados VIP: ")
    if perg != "fim": 
        triagem.append(perg)
for pessoa in triagem:
    if pessoa[0] == "a":
        lista_vip.append(pessoa)
print("As pessoas que atenderam os requisitos para adentrar na lista VIP são: ", lista_vip)