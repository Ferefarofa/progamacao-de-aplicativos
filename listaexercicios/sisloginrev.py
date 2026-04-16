secreta = 123
senha = input("Digite a senha: ")
tentativas = 1
while tentativas < 3 and senha != 123:
    tentativas = tentativas + 1
    print(f"Tente de novo!, tentativa: {tentativas}")
    senha = input("Digite a senha: ")
if tentativas == 3 and senha != secreta:
    print("Acesso bloqueado!")
elif tentativas < 4 and senha == secreta:
    print("Acesso liberado")