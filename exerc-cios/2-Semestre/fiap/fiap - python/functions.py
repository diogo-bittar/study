# #antes sem lógica
# modos_camera = {
# "noturno": "melhora fotos com pouca luz",
# "retrato": "destaca pessoas",
# "documento": "melhora leitura de textos"
# }
# modo = input("Modo: ")
# if modo in modos_camera:
#     print(modos_camera[modo])
# else:
#     print("Modo não cadastrado")


# #depois com lógica
# def consultar_modo(modos, modo):
#     if modo in modos:
#         return modos[modo]
#     return "Modo não cadastrado"
# modos_camera = {
# "noturno": "melhora fotos com pouca luz",
# "retrato": "destaca pessoas",
# "documento": "melhora leitura de textos"
# }
# print(consultar_modo(modos_camera, "noturno"))


# exercise

# # Sem função:
# recurso = input("Recurso: ")
# if recurso in configuracoes:
#     print(configuracoes[recurso])
# else:
#     print("Recurso não encontrado")

# """
# Crie uma função chamada consultar_recurso(configuracoes, recurso).
# A função deve receber o dicionário e o nome do recurso.
# Se existir, deve retornar a explicação.
# Se não existir, deve retornar uma mensagem de erro simples
# """

# configuracoes = {
# "grade": "ativa linhas de apoio na tela",
# "hdr": "equilibra áreas claras e escuras",
# "timer": "atrasa o disparo da foto"
# }

# def consultar_recurso(configuracoes, recurso):
#     if recurso in configuracoes:
#         return configuracoes[recurso]
#     return "error"

# print(consultar_recurso(configuracoes, input("informe o modo: ")))

# modos ={
#     "noturno": "pouca luz",
#     "retrato": "destaca pessoas"
# }

# def consultarModo(dados, chave):
#     if chave in dados:
#         return dados[chave]
#     return None

# print(consultarModo(modos, "oi"))

# Base de trabalho
# Crie uma função chamada gerarMsg


# A função deve receber um parâmetro chamado estudante
# com valor padrão True.
# Se estudante for True:
# retorne "Modo simples ativado"
# Se estudante for False:
# retorne "Modo avançado ativado"
# Teste:
# def gerarMsg(estudante=True):
#     if estudante == True:
#         return "Modo simples"
#     return "Modo avançado"

# print(gerarMsg())
# print(gerarMsg(estudante=False))



# def avaliar_recurso(nome, clareza, utilidade, facilidade):
#     media = (clareza + utilidade + facilidade) / 3
#     return nome, media


# resultado = avaliar_recurso(
#     nome="modo estudo",
#     clareza=8,
#     utilidade=9,
#     facilidade=7
# )
# print(resultado)
# resultado_noturno = avaliar_recurso(
#     nome="modo noturno",
#     clareza=9,
#     utilidade=9,
#     facilidade=5
# )
# print(resultado_noturno)


modos_camera = {
"noturno": {
"uso": "ambientes com pouca luz",
"dificuldade": 2
},
"retrato": {
"uso": "fotos de pessoas",
"dificuldade": 2
},
"documento": {
"uso": "fotos de textos e quadros",
"dificuldade": 1
},
"esporte": {
"uso": "movimento rápido",
"dificuldade": 3
}
}
avaliacoes = [8, 9, 7, 10]

# def consulteModo(modo, modos):
#     if modo in modos:
#         return modos[modo]
#     return "Não encontrado"

# print(consulteModo("retrato", modos_camera))


def recomendarModo(mode):
    if mode in modos_camera and modos_camera[mode]["dificuldade"] == 1:
        return f"Recomendo o modo: {mode}"
    elif mode in modos_camera and modos_camera[mode]["dificuldade"] == 2:
        return f"O modo {mode} tem dificuldade média"
    elif mode in modos_camera and modos_camera[mode]["dificuldade"] == 3:
        return f"O modo {mode} é difícil de usar"
    return "Modo não encontrado"

print(recomendarModo("documento"))
print(recomendarModo("retrato"))
print(recomendarModo("noturno"))
print(recomendarModo("esporte"))

def resumoAvaliacao(avs):
    avs = sum(avs) / 4
    return avs

print(resumoAvaliacao(avaliacoes))