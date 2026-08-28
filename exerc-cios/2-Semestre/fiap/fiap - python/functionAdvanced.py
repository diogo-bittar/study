"""
Aula de funções avançadas II
"""
#*args

# def mostrar_recursos(*args):
#     print(args)
# mostrar_recursos("hdr", "grade")
# mostrar_recursos("hdr", "grade", "timer", "foco")
# mostrar_recursos("hdr", "grade", "timer", "foco", "nitidez")


# def ativar_recursos(*recursos):
#     for recurso in recursos:
#         print("Ativar:", recurso)
# ativar_recursos("hdr")
# ativar_recursos("hdr", "grade", "timer")


# def listRecurses(*recurses):
#     lists = []
#     for r in recurses:
#         lists.append(r)
#     return lists 
# print(listRecurses("hdr", "grade"))
# print(listRecurses("timer", "foco", "zoom"))


# def sumAv(*notes):
#     sum(notes)
#     return f"Soma total de notas: {notes}"

# print(sumAv(8, 9))
# print(sumAv(8, 9, 7, 10))
# #---------------

# # **kwargs
# def mostrar_configuracoes(**kwargs):
#     print(kwargs)
# mostrar_configuracoes(
# modo="noturno",
# qualidade="alta",
# flash=False
# )

# def mostrar_configuracoes(**config):
#     for chave in config:
#         print(chave, ":", config[chave])

# mostrar_configuracoes(
# modo="noturno",
# qualidade="alta",
# flash=False
# )
# mostrar_configuracoes(
# modo="retrato",
# foco="rosto"
# )

# def registreConfig(**dados):
#     for chave in dados:
#         print(f"{chave}: {dados[chave]}")

#     return "Configurações registradas"

# print(registreConfig(modo="noturno", 
# flash=False))

# print(registreConfig(modo="retrato", 
# foco="rosto", timer=3))


# def montarPerfil(**opcs):
#     idioma = opcs.get("idioma", "pt-BR")
#     tema = opcs.get("tema", "claro")
#     notificacao = opcs.get("notificacao", True)

#     return idioma, tema, notificacao

# print(montarPerfil(user="Diogo"))
# print(montarPerfil(user="Bittar", tema="escuro", notificacao="False"))


#lambda 
quadrado = lambda x: x ** 2

maiusculo = lambda texto: texto.upper()

status = lambda nota: "aprovado" if nota >= 7 else "revisar"
print(quadrado(4))
print(maiusculo("jovi"))
print(status(8))
print(status(5))


dobro = lambda num: num * 2
firstLetra = lambda text: text[0]
nivel = lambda nota: "alto" if nota >= 8 else "baixo"

print(dobro(2))
print(firstLetra("oi"))
print(nivel(7))
print(nivel(9))


#lista para treinar (aula)
def listarModos(*modos):
    listaVazia = []
    for l in modos:
        listaVazia.append(l)
    return listaVazia
print(listarModos("hdr", "grade"))
print(listarModos("timer", "foco", "zoom"))

def resumoConfig(**config):
    return len(config)

def totalPoints(*points):
    return sum(points)


passou = lambda nota: nota >= 7 