#classes e objetos


#exemplo
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def buzinar(self):
        print(f"{self.marca} buzinando: BEEP")

meu_carro = Carro("Toyota", "Corolla")
meu_carro.buzinar()

#exercicio 1
class Livro:
    def __init__(self, titulo, autor, paginas, lido: bool):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.lido = lido

    def marcarComoLido(self):
        self.lido = False
        print(f"{self.titulo}, de {self.autor}, foi marcado como lido: {self.lido}")

title = Livro("POO", "DIOGO", 99, True)
title.marcarComoLido()

# #exercicio 2
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

# #ex 3
class Funcionario:
    empresa = "Amazon"

    def __init__(self, nome):
        self.nome = nome

shopee = Funcionario("Shopee")
magalu = Funcionario("Magalu")

print(shopee.empresa, magalu.empresa)
Funcionario.empresa = "Mercado Livre"
print(shopee.empresa, magalu.empresa)

shopee.empresa = "Aliexpress"
print(shopee.empresa, magalu.empresa)        

#ex 4
class Acessorios:
    def __init__(self, marca, gigas, cor):
        self.marca = marca
        self.gigas = gigas
        self.cor = cor 

listaAcessorios = []
lenovo = Acessorios("lenovo", 64, "azul")
positivo =  Acessorios("positivo", 32, "branco")
asus = Acessorios("asus", 128, "prata")

listaAcessorios.extend([lenovo, positivo, asus])

for i in listaAcessorios:
    print(f"Marca: {i.marca}\nGigas: {i.gigas}\nCor: {i.cor}\n ")

#ex integrador do módulo
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def venderProduto(self, qtd):
        if qtd > self.estoque:
            return "Estoque insuficiente"
        self.estoque -= qtd
        return f"Você vendeu {qtd}."

    def reporProduto(self, qtd):
        if qtd <= 0:
            return "Quantidade inválida para reposição"
        self.estoque += qtd
        return f"Estoque foi reposto para {self.estoque}"


notebook = Produto("Notebook", 3200, 10)

print(notebook.venderProduto(3))   
print(notebook.estoque)            

print(notebook.venderProduto(50))  
print(notebook.estoque)            

print(notebook.reporProduto(20))    
print(notebook.estoque)             

print(notebook.reporProduto(-5))    
print(notebook.estoque)             


