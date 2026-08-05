"""
Aula sobre argumentos em funções

Argumentos nomeados e não nomeados 

A.Nomeado --> possui nome com sinal de igual //
A.N.Nomeado --> recebe apenas o argumento (valor) //
"""

#x e y --> argumentos posionais 
def soma(x, y):
    #Aqui temos a definição
    print(f'{x=}, {y=}', '|', 'x + y =', x + y)

soma(1, 4) #aqui são os valores que eu atribuo 