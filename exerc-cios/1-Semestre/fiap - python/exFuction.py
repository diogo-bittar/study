"""
Aula sobre funções --> def
Aula foi sobre exercícios de listas
"""
# ex 1 // dificuldade foi lembrar do len para definir o tamanho da lista e ter apenas 10 numeros
import random
lista = []

while len(lista) < 10:
    n = random.randint(1, 20)
    if n not in lista:
        lista.append(n)
print(lista)
#-------------------------------------#
#ex 2  // tive uma dificuldade para executar a parte dos numeros primos
trinta = []
primos = []

for i in range(30):
    trinta.append(random.randint(1, 50))
print(trinta)

for numero in trinta:
    if numero >= 2:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
        if primo:
            primos.append(numero)
print(f'Primos: {primos}')
#--------------------------------#
#ex 3  // 
list = []

for i in range(30):
    list.append(random.randint(1, 50))

inteiro = int(input('Informe um número INTEIRO: '))

multiplicacao = []
for i in range(len(list)):
    multiplicacao.append(list[i] * inteiro)

print(list)
print(f'Lista Multiplicada: {multiplicacao}')
#------------------------------------------------#
#ex 4 
list4 = []
for i in range(10):
    add = int(input('Informe um número que seja inteiro: '))
    list4.append(add)

palindromo = True
for i in range(5):
    if list4[i] != list4[9 - i]:
        palindromo = False

print(list4)
print( palindromo)


#ex 5 // o mais tranquilo, gerar os numeros e dps criar uma outra lista para implementar os 20 numeros
lista5 = []
lista6 = []
lista20 = []
for i in range(10):
    lista5.append(random.randint(1, 10))

for i in range(10):
    lista6.append(random.randint(1, 10))

for i in range(10):
    lista20.append(lista5[i])
    lista20.append(lista6[i])
print(lista20)
#------------------------------------------------#
#Preciso melhorar meu pensamento e lógica.