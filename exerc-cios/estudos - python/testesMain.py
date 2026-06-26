from teste import *

while True:
    print("\n\t---|MENU|---\n")
    print("(1) - Adicionar uma tarefa")
    print("(2) - Listar tarefas")
    print("(3) - Atualizar uma tarefa")
    print("(4) - Remover uma tarefa")
    print("(5) - Sair do gerenciador de tarefas")
    print("-" * 30)

    opcao = input("Escolha uma opção válida: ")
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
            print("Até breve! :)\nSistema encerrando...")
            break
        case _:
            print("Opção inválida.\nDigite um dos número válidos (1 / 2 / 3 / 4 / 5)")