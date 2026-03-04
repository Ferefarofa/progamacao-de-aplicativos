cargo = input("Insira o seu cargo: ")
code = int(input("Código de acesso: "))
botao = input("Botão de emergencia pressionado?(s/n): ")
epi = input("EPI completo?(s/n): ")

if (cargo == "ENGENHEIRO" or "TECNICO") and (code == 1234 or botao == "s") and epi == "s":
    print("ACESSO LIBERADO. ")
else:
    print("ACESSO NEGADO: RISCO DE SEGURANÇA. ")

