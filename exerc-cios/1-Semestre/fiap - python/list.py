"""
Aula sobre Listas --> FIAP
"""
#Criando uma lista qualquer que contém nomes 
#           0       1       2        3
nomes = ['Paulo', 'Ana', 'Pedro', 'Maria']

for i in range(len(nomes)):
    print(nomes[i])

#pop REMOVE da lista
nomes.pop(-1)
print(nomes)


#---------------------------------------
numero = []

while True:
    n = int(input('Informe um número: '))
    if n == 0:
        break
    numero.append(n)
    
print(numero)