matriz = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11]
]

encontrado = False
number = int(input("Digite o número que deseja buscar no tabuleiro: "))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == number:
            encontrado = True
            print(f'\nO número encontrado na Posição: Linha {i}, Coluna {j}.')
            break

if encontrado == False:
    print(f'\nO número {number} está fora da matriz...\n'
          f'\n\tA matriz original:\n {matriz}')