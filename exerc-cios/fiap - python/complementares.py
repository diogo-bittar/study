"""
Exercícios Complementares: Funções
"""

#1. Crie uma função que receba três números como parâmetros, e retorne True se a 
# soma de quaisquer pares de números gera a soma do terceiro número. Caso 
# contrário retorne False

def num(a, b, c):
    return a + b == c or a + c == b or b + c == a

# print(num(2, 3, 6))

#2. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Por exemplo: 
# 120 é triangular, pois 4 * 5 * 6 = 120. 
# 2730 é triangular, pois 13 * 14 * 15 = 2730. 
# Faça uma função que receba um número inteiro e retorne True se for um número triangular e False, caso contrário.

def triangular(numero):
    n = 1
    while n * (n + 1) * (n + 2) < numero:
        n += 1
    return n * (n + 1) * (n + 2) == numero

# print(triangular(210))

