"""
Fuctions 1a class
"""

def hello(msg, nome):
    return f'{msg}, {nome}!'

def execution(fuction, *args):
    return fuction(*args)


variable = execution(hello, 'Good morning', 'Diogo')
