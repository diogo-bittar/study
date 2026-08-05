"""
Exercícios sobre funções
"""

#Crie uma def que multiplica todos os argumentos não nomeados
#Retorne o total da variavel e mostre o valor da variavel

def multiplicaNumero(*args):
    total = 1
    for numero in args:
        total *= numero
    return total 

resultado = multiplicaNumero(1,2,3,4,5)
print(resultado)

#Criar uma def que retorne se um numero é par ou ímpar.
def parImpar(numero):
    multiploDois = numero % 2 == 0

    if multiploDois:
        return f'{numero} é par.'
    return f'{numero} é ímpar.'


print(parImpar(27))
print(parImpar(2))

