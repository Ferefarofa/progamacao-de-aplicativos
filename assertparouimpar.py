def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um numero para descobrir se é par ou impar: "))
eh_par(numero)
assert eh_par(4) == True
assert eh_par(5) == False
assert eh_par(0) == True
assert eh_par(-6) == True
assert eh_par(-5) == False
