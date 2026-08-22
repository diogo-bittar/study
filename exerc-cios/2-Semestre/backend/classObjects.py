#classes e objetos


#exemplo
# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo

#     def buzinar(self):
#         print(f"{self.marca} buzinando: BEEP")

# meu_carro = Carro("Toyota", "Corolla")
# meu_carro.buzinar()

#exercicio 1
class Livro: 
    def __init__(self, titulo, autor, paginas, lido:bool):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = lido

    def marcarComoLido(self):
        self.lido= True
        print(f"{self.titulo} tem {self.paginas}? {self.lido}")

title = Livro("POO", "DIOGO", 100, False)
title.marcarComoLido()

#exercicio 2
class ContaBancaria:
    def __init__(self, valor):
        self.valor = valor

    def depositar(self, valor):
        if valor == 0 or valor < 0:
            return "valor não disponivel"
        self.valor += valor
        return f"vc depositou {self.valor}"

    def sacar(self, valor):
        if valor > self.valor or valor == 0 or valor < 0:
            return "o valor de saque nao condiz com o saldo ou ficou zerado"
        self.valor -= valor
        return f"Você sacou {valor}.\nSaldo restante {self.valor}."

deposito = ContaBancaria(155)
print(deposito.depositar(100))
print(deposito.sacar(50))