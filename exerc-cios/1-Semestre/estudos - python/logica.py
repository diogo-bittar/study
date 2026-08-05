# matriz = [
#     [1, 5, 9],
#     [2, 6, 10],
#     [3, 7, 11]
# ]

# encontrado = False
# number = int(input("Digite o número que deseja buscar no tabuleiro: "))

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] == number:
#             encontrado = True
#             print(f'\nO número encontrado na Posição: Linha {i}, Coluna {j}.')
#             break

# if encontrado == False:
#     print(f'\nO número {number} está fora da matriz...\n'
#           f'\n\tA matriz original:\n {matriz}')


# Exs 2)

matriz = [
    #0  1   2
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m = len(matriz)

matrizNova = [[0] * m for _ in range(m)]

for i in range(m):
    for j in range(m):
        matrizNova[j][m - 1 - i]  = matriz[i][j]

for linha in matrizNova:
    print(linha)