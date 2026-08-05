""""
Aula introdutória sobre def / funções
Funções são trechoes de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e
retornar um valor específico 
"""

def imprimir(a, b, c):  #parâmetro se refere ao que está dentro dos ()
    ...


def saudacao(nome):
    print(f'Olá, {nome}!')

nome = input('Digite o seu nome: ').upper()
saudacao(nome)


def multiploDe(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

multiploDe(16, 8)
multiploDe(15, 3)
multiploDe(10, 5)
