codigo = int(input("Digite o código do drone: "))
autorizacao = input("\nPossui autorização ?(s/n): ")
if (codigo == 999 or autorizacao == "s"):
    bateria = int(input("\nQual o nivel de bateria ?(0-100): "))
    clima = input("\nComo está o clima ?(ensolarado/chuvoso): ")
    vento = int(input("\nQual a velocidade do vento ?(km/h): "))
    if bateria <= 10:
        print("\nBATERIA BAIXA! Pouso emergencial autorizado.")
    
    elif (bateria > 10 and clima == "ensolarado" and vento < 30) or (bateria > 10 and clima == "chuvoso" and vento < 10):
        print("Pouso autorizado, iniciando descida.")

    else:
        print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")
else:
    print("ERRO 01: Drone não indentificado. Retornando à base.")


