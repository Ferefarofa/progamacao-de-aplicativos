secreta = ["azul", "preto", "verde"]
print("Jogo de adivinhação, você tem 3 tentativas para acertar uma das cores presentes na lista!")
palpite = input("Dê o seu palpite (Tentativa 1): ")
tentativas = 1
while tentativas < 3 and palpite not in secreta:
    tentativas = tentativas + 1
    print(f"Tente de novo!, tentativa: {tentativas}")
    palpite = input("Dê o seu palpite: ")
if tentativas == 3 and palpite not in secreta:
    print(f"Que pena, você nao acertou as cores, elas eram: {secreta}")
elif tentativas < 4 and palpite in secreta:
    print(f"Parabéns, você acertou uma das cores!, elas eram: {secreta}")