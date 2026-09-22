def frete_gratis(valor):
    if valor >= 200:
 	    return True
    return False



frete_gratis(201)
assert frete_gratis(199.99) == False
assert frete_gratis(200) == True
assert frete_gratis(200.01) == True

def pode_votar(idade):
    if idade >= 16:
        return True
    return False


pode_votar(14)
assert pode_votar(15) == False
assert pode_votar(16) == True
assert pode_votar(17) == True



def senha_valida(senha):
    if len(senha) >= 8:
        return True
    return False

senha = "abec"
senha_valida(senha)
assert senha_valida("aaaaaaa") == False
assert senha_valida("aaaaaaaa") == True
assert senha_valida("aaaaaaaaa") == True
