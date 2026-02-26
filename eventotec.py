print("Bem vindo ao tecnology event, você deve responder as seguintes perguntas para saber se você cumpre os requisitos para adentrar no evento ")
print(" ")
idade = int(input("Qual a sua idade ?: "))
saldo = float(input("QUal o saldo disponivel na sua carteira ?: "))
if idade >= 18 and saldo >= 50:
    print("Acesso autorizado, Bem vindo(a) ao evento! ")
else:
    print("Infelizmente você nao cumpre os requisitos de entrada")
    