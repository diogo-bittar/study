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
    ...

def removerJogos():
    