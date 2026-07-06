from funcoes import perguntar, inserir, pesquisar, excluir, listar

usuarios = {}

while True:
    opcao = perguntar()

    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios)
    elif opcao == "E":
        excluir(usuarios)
    elif opcao == "L":
        listar(usuarios)
    elif opcao == "S":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Digite I, P, E, L ou S.\n")