estoque = []
acao = 0

def adicionar_produto(nome): #É uma função que não recebe valores válidos em seus parâmetros, seu valor se torna útil quando o usuário o altera no input dentro da função. É a função responsavel por adicionar itens na lista(estoque).
    nome = input("Digite o nome do produto: ")
    estoque.append(nome)

def listar_produtos(estoque): #É uma função que recebe predefinidamente a lista "estoque" em seus parâmetros, lista os itens presentes dentro da lista e seus respectivos índices.
    for item in estoque:
        print(f"\n{estoque.index(item)} - {item}")

def atualizar_produto(indice, produto): #É uma função que não recebe valores válidos em seus parâmetros[...]. É uma função responsavel por atualizar valores dentro da lista.
    indice = int(input("Qual o indice do produto ?: "))
    produto = input("Qual o nome do produto ?: ")
    estoque[indice] = produto

def remover_produto(indice): #É uma função que não recebe valores válidos em seus parâmetros[...]. É uma função responsavel por remover algum produto da lista pelo índice.
    indice = int(input("Qual o indice do produto a ser removido ?: "))
    removido = estoque[indice]
    estoque.pop(indice)
    print(f"Item {removido} removido. ")

def exibir_menu(acao): #Função coração do programa, executa todas as outras funções anteriores e coloca o programa em funcionamento.
    while acao != 5:
        print("\n1 - Adicionar produto")
        print("\n2 - Listar produtos ")
        print("\n3 - Atualizar produto ")
        print("\n4 - Remover produto ")
        print("\n5 - Fechar menu")
        acao = int(input("Qual ação deseja realizar ?: "))

        if acao == 1:
            adicionar_produto(acao)
        elif acao == 2:
            listar_produtos(estoque)
        elif acao == 3:
            atualizar_produto(acao, acao)
        elif acao == 4:
            remover_produto(acao)
        elif acao == 5:
            return
        
exibir_menu(acao)
print("Menu fechado. ")