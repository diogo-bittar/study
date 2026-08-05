"""
Aula 2 de Listas -- Exercícios 
"""

#Exercício 1 

lista = [10, 100, 20, 200, 30, 300]

min = lista[0]  
max = lista[0]

for i in lista:
    if min > i:
        min = i 
    elif max < i:
        max = i 

print(f'O menor número é {min}')
print(f'O maior número é {max}')