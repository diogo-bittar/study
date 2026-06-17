"""
Sistema CRUD - Biblioteca de Jogos

Objetivo:
Desenvolver um sistema de gerenciamento de jogos utilizando listas.

Cada jogo deve conter:
- Nome
- Gênero
- Ano de lançamento
- Desenvolvedora

Funcionalidades:
1. Cadastrar um novo jogo.
2. Listar todos os jogos cadastrados.
3. Atualizar os dados de um jogo existente.
4. Remover um jogo da biblioteca.

Requisitos:
- Utilizar apenas listas.
- Criar uma função para cada operação do CRUD.
- Exibir mensagens informando o resultado de cada ação.
"""
from functions import *

print("=" * 50)
print("\tBem-vindo à Biblioteca de Jogos!")
print("\tGerencie seus games favoritos conosco.")
print("=" * 50)

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar jogo")
    print("2 - Listar jogos")
    print("3 - Atualizar jogo")
    print("4 - Remover jogo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: \n")

    match opcao:
        case "1":
            cadastrarJogo()
        case "2":
            print(listarJogos())
        case "5":
            print("Encerrando o sistema...")
            break
        case _:
            print("Opção inválida! Escolha uma opção entre 1 e 5.")