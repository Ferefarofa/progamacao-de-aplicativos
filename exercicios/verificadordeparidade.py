def eh_par(numero):
    if numero % 2 == 0:
        numero = True
    elif numero % 2 != 0:
        numero = False
    if numero == True:
        print("O número é par. ")
    else:
        print("O número é ímpar. ")
numero_a_definir = int(input("Digite um número para saber se é par ou ímpar: "))
eh_par(numero_a_definir)