jogos = []

def cadastrarJogo():
    nomeJogo = input("Informe o nome do jogo que deseja cadastrar: ")
    generoJogo = input("Qual o gênero deste jogo?: ")

    while True:
        try:
            anoLancamento = int(input("Qual o ano de lançamento desse jogo?: "))

            if anoLancamento <= 0:
                print("Ops, precisa ser um ano válido.")
                continue

            break

        except ValueError:
            print("Ops, precisa ser um ano válido.")

    desenvolvedora = input("Quem é a desenvolvedora?: ")

    jogos.append([nomeJogo, generoJogo, anoLancamento, desenvolvedora])

def listarJogos():
    if not jogos:
        return "Poxa, nenhum jogo cadastrado!\nQue tal adicionar um novo jogo? :)"
    
    texto = ""

    for jogo in jogos:
        texto += f"Nome: {jogo[0]}\nGênero: {jogo[1]}\nAno: {jogo[2]}\nDesenvolvedora: {jogo[3]}\n"
    return texto

def atualizarJogos():
    if not jogos:
        return "Ops, nenhum jogo para atualizar."
    nomeJogo = input("Digite o nome do jogo que você deseja atualizar: ")

    for jogo in jogos:
        if jogo[0].lower() == nomeJogo.lower():
            jogo[0] = input("Novo nome: ")
            jogo[1] = input("Novo gênero: ")

            while True:
                try:
                    ano = int(input("Novo ano de lançamento: "))

                    if ano <= 0:
                        print("Ops, precisa ser um ano válido.")
                        continue

                    jogo[2] = ano
                    break

                except ValueError:
                    print("Ops, precisa ser um ano válido.")

            jogo[3] = input("Nova desenvolvedora: ")

            return "Jogo atualizado com sucesso! :)"

    return "Jogo não encontrado."

def removerJogos():
    if not jogos:
        return "Ops, nenhum jogo para remover."

    nomeJogo = input("Digite o nome do jogo que você deseja remover: ")

    for jogo in jogos:
        if jogo[0].lower() == nomeJogo.lower():
            jogos.remove(jogo)
            return "Jogo removido com sucesso! :)"

    return "Jogo não encontrado."