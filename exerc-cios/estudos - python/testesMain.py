from teste import *

while True:
    print("\n\t--- MENU ---\n")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar uma tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("-" * 50)

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            taskAdd()
        case "2":
            print(listTask())

        case "3":
            print(atualizarTask())

    #     case "4":
    #         print(removerJogos())

        case "5":
            print("Encerrando o sistema...")
            break
        case _:
            print("Opção inválida! Escolha uma opção entre 1 e 5.")