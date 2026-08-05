""""
Aula sobre valores padrão em parâmetros

Ao definir um função, os parâmetros podem ter valores padrão.
Caso  valor não seja enviado para o parâmetro, o valor padrão será usado.
"""

def soma(x, y, z=None):
    if z is not None: #verifico se o Z não é None
        print(f'{x=} {y=} {z=} ', x + y + z)
    else: #Se for None. exibo sem o Z
        print(f'{x=} {y=}', x + y)


soma(1, 7)
soma(1, 70, 0)
soma(1, 7)