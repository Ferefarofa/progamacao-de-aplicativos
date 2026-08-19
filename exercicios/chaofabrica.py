print("Para operar a Prensa Hidráulica, o aprendiz precisa de curso e supervisão.")
curso = input("Você concluiu o curso de segurança?(s/n): ")
if curso == "n":
    print("Acesso negado, faça o treinamento primeiro. ")
elif curso == "s":
    instrutor = input("O intrutor está presente na sala?(s/n): ")
    if instrutor == "n":
        print("Aguarde o instrutor para ligar a maquina.")
    elif instrutor == "s":
        print("Acesso liberado! Operação iniciada.")
