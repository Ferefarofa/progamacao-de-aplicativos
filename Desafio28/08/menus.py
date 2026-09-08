def menu_escolas():
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR ESCOLA\n 2 - LISTAR ESCOLAS\n 3 - ATUALIZAR ESCOLAS\n 4 - REMOVER ESCOLAS\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_escola()
            elif opcao == 2:
                listar_escolas()
            elif opcao == 3:
                atualizar_escola()
            elif opcao == 4:
                remover_escola()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_escolas()
        elif opcao == 5:
            print("Fechando menu das escolas")
        else:
            menu_escolas()