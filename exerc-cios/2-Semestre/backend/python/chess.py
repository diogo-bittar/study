"""
Exercitando os conhecimentos em POO e Herança

Sistema de Validação de Peças em Xadrez
"""

class Peca():
    def __init__(self, cor, posicao: tuple):
        self.cor = cor
        self.posicao = posicao

    def movimentoValido(self, destino: tuple):
        return False
    


        