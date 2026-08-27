import sqlite3
conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

from redes import cadastrar_rede, listar_redes, atualizar_rede, remover_rede, menu_redes

from lojas import cadastrar_loja, listar_lojas, atualizar_loja, remover_loja, menu_lojas

def menu_principal():
    try:
        acao = 0
        while True:
            print(" SISTEMA DE MERCADOS PARANAVAÍ")
            print("==================================\n 1 - MENU DE REDES\n 2 - MENU DE LOJAS\n 3 - ENCERRAR SISTEMA\n==================================\n")
            acao = int(input("Digite a opção do menu para acessar: "))
            if acao == 1:
                menu_redes()
            elif acao == 2:
                menu_lojas()
            elif acao == 3:
                break
            elif acao not in (1, 2, 3):
                print("Insira uma opção válida")
        print("Volte sempre!")
        
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if acao != 3:
            print("Tente novamente")
            menu_principal()
        elif acao == 3:
            print("Fechando menu principal")
        else:
            menu_principal()




menu_principal()