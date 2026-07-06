def perguntar():
    return input(
        "O que você deseja fazer?\n"
        "(I) --> Inserir um usuário.\n"
        "(P) --> Pesquisar um usuário.\n"
        "(E) --> Excluir um usuário.\n"
        "(L) --> Listar todos os usuários.\n"
        "(S) --> Sair.\n"
        "Escolha: "
    ).strip().upper()


def inserir(dicionario):
    login = input("Digite o login: ").strip().upper()
    if not login:
        print("Login inválido. Tente novamente.\n")
        return

    nome = input("Digite o nome do usuário: ").strip().upper()
    ultimo_acesso = input("Data de último acesso: ").strip()
    estacao = input("Qual a última estação acessada?: ").strip().upper()

    dicionario[login] = [nome, ultimo_acesso, estacao]
    print(f"Usuário {login} inserido com sucesso.\n")


def pesquisar(dicionario):
    login = input("Digite o login para pesquisar: ").strip().upper()
    usuario = dicionario.get(login)
    if usuario is None:
        print("Usuário não encontrado.\n")
        return

    nome, acesso, estacao = usuario
    print(f"Login: {login}\nNome: {nome}\nÚltimo acesso: {acesso}\nEstação: {estacao}\n")


def excluir(dicionario):
    login = input("Digite o login para excluir: ").strip().upper()
    if login in dicionario:
        del dicionario[login]
        print(f"Usuário {login} excluído com sucesso.\n")
    else:
        print("Usuário não encontrado.\n")


def listar(dicionario):
    if not dicionario:
        print("Nenhum usuário cadastrado.\n")
        return

    for login, (nome, acesso, estacao) in dicionario.items():
        print(f"Login: {login}\nNome: {nome}\nÚltimo acesso: {acesso}\nEstação: {estacao}\n")