from teste import *

while True:
    print("\n--- MENU ---\n")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar uma tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("-" * 30)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            taskAdd()

        case "2":
            print(listTask())

        case "3":
            print(atualizarTask())

        case "4":
            removeTask()

        case "5":
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida.")