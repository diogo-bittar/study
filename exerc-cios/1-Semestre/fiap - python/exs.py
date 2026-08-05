"""
Exercícios da aula de listas -- 27/04
RM569657 -- DIOGO BITTAR PEDRO
1ESPY
"""
#EX 1
"""lista_pares = []
lista_impares = []
cont = 0 

for i in range(1,11,1):
    cont =+ 1
    numeros = int(input('Informe um número: '))
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)

print(lista_impares)
print(lista_pares)
"""

#EX 2
"""par = []
numeros = []
for i in range(1,11,1):
    number = int(input('Informe a nota: '))
    numeros.append(number)
    if number % 2 == 0:
        par.append(number)

print(len(numeros)/(sum(numeros)))
print(sum(par))
"""

#EX 3
"""import random

list = []
n = random.randint(1,50)
for i in range(20):
    n = random.randint(1, 50)
    list.append(n)

print(list)
print(sum(list))
print(max(list))
print(min(list))"""



