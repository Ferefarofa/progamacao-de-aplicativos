usuario = input("Usuário: ")
senha = int(input("Senha: "))
if usuario == ("admin" or "root") and senha == 12345:
    print("Acesso liberado")
else:
    print("Acesso negado")