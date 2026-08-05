"""
Escopos
"""

x = 1 #essa variável esta no escopo do arquivo 


def escopo():
    x = 10 #essa variável esta protegida pela função e só pode ser acessada quando chamada
    print(x)
    def outro_escopo():
        global x
        x = 11 #global serve para manipular a variavel de fora, agora passei um outro valor
        y = 2
        print(y, x)
    outro_escopo()


print(x)
escopo()

