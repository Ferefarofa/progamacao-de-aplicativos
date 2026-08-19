print("Você pode efetuar 3 operações: ")
print("deposito")
print("saque")
print("extrato")
saldo = 1000
operacao = input("Qual operação você irá realizar: ")
if operacao == "deposito":
    deposito = float(input("Qual o valor você irá depositar? R$: "))
    valorfinal = saldo + deposito
elif operacao == "saque":
    saque = float(input("Qual o valor do saque? R$: "))
    valorfinal = saldo - saque
elif operacao == "extrato":
    valorfinal = saldo

if operacao == ("deposito" or "saque") and valorfinal != saldo:
    print("Seu saldo agora é R$:", valorfinal)
elif operacao == "extrato":
    print("Seu saldo agora é R$:", valorfinal)
else:
    print("Operação inválida.")






