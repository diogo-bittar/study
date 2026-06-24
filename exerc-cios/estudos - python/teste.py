import time

task = []

def validText(text):
    return text.strip() != ""

def validStatus(status):
    status = status.strip().lower()
    return status in ["feito", "em andamento", "não realizada"]

def taskAdd():
    while True:
        taskName = input("Nomeie essa tarefa: ").strip()

        if not validText(taskName):
            print("Ops, nome inválido!")
            continue

        # impede duplicados
        for t in task:
            if t[0].lower() == taskName.lower():
                print("Já existe uma tarefa com esse nome.")
                continue

        taskContent = input("Qual conteúdo essa tarefa se encaixa?: ")

        if not validText(taskContent):
            print("Ops, conteúdo inválido!")
            continue

        while True:
            status = input("Status (Feito / Em andamento / Não realizada): ")

            if validStatus(status):
                task.append([
                    taskName,
                    taskContent.strip(),
                    status.strip().capitalize(),
                    time.strftime("%d/%m/%Y %H:%M:%S")
                ])
                print("Tarefa adicionada com sucesso.")
                return

            print("Status inválido! Tente novamente.")

def listTask():
    if not task:
        return "Nenhuma tarefa foi listada...\nQue tal listar alguma?"

    texto = ""

    for t in task:
        texto += (
            f"Nome: {t[0]}\n"
            f"Conteúdo: {t[1]}\n"
            f"Status: {t[2]}\n"
            f"Criada em: {t[3]}\n\n"
        )

    return texto

def atualizarTask():
    if not task:
        return "Nenhuma tarefa para atualizar."

    taskName = input("Digite o nome da tarefa que deseja atualizar: ")

    for t in task:
        if t[0].lower() == taskName.strip().lower():

            while True:
                novoStatus = input("Novo status (Feito / Em andamento / Não realizada): ")

                if validStatus(novoStatus):
                    t[2] = novoStatus.strip().capitalize()
                    return "Status da tarefa atualizado com sucesso."

                print("Status inválido! Tente novamente.")

    return "Tarefa não encontrada."

def removeTask():
    if not task:
        return "Nenhuma tarefa para remover."

    taskName = input("Informe qual tarefa você deseja remover: ")

    for t in task:
        if t[0].lower() == taskName.strip().lower():
            task.remove(t)
            print("Tarefa removida com sucesso.")
            return

    return "Tarefa não encontrada."