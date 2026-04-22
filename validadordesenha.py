def senha_valida(senha):
    while len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres, insira senha novamente.")
        senha = input("Crie sua senha: ")
    print("Senha definida com sucesso!")
    return senha

senha = input("Crie a senha:")
senha_cadastrada = senha_valida(senha)