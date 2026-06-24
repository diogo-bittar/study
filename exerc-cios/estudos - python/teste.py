task = []

def validText(text):
    return text.strip() != ""

def validStatus(status):
    status = status.strip().lower()
    return status in ["feito", "em andamento", "não realizada"]

def taskAdd():
    while True:
        taskName = input("Nomeie essa tarefa: ")

        if not validText(taskName):
            print("Ops, nome inválido!")
            continue

        taskContent = input("Qual conteúdo essa tarefa se encaixa?: ")

        if not validText(taskContent):
            print("Ops, conteúdo inválido!")
            continue

        while True:
            status = input("Status (Feito / Em andamento / Não realizada): ")

            if validStatus(status):
                task.append([
                    taskName.strip(),
                    taskContent.strip(),
                    status.strip().capitalize()
                ])
                print("Tarefa adicionada com sucesso.")
                return

            print("Status inválido! Tente novamente.")


def listTask():
    if not task:
        return "Nenhuma tarefa foi listada...\nQue tal listar alguma?"

    texto = ""

    for t in task:
        texto += f"Nome: {t[0]}\nConteúdo: {t[1]}\nStatus: {t[2]}\n\n"

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