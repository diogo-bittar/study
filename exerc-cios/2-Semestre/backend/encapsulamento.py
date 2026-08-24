"""
Módulo 2 - Encapsulamento
"""

#exemplo 
class ProdutoExemplo:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor

p = ProdutoExemplo(10)
p.preco = -5  # aqui o programa para e mostra o ValueError


#ex 1
class ContaBancaria:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def depositar(self, valor):
        if valor == 0 or valor < 0:
            raise ValueError("Valor de depósito inválido")
        self._valor += valor
        return f"vc depositou {self._valor}"

    def sacar(self, valor):
        if valor > self._valor or valor == 0 or valor < 0:
            raise ValueError("Valor de saque inválido ou saldo insuficiente")
        self._valor -= valor
        return f"Você sacou {valor}.\nSaldo restante {self._valor}."


deposito = ContaBancaria(155)
print(deposito.depositar(100))   # funciona normal, imprime a confirmação
print(deposito.sacar(50))        # funciona normal, imprime a confirmação

deposito.sacar(-10)              # aqui o programa PARA e mostra o ValueError
print("essa linha nunca roda")   # porque o raise acima interrompeu tudo

#ex 2
class Pessoa():
    def __init__(self, idade):
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            raise ValueError("Idade negativa não pode")
        self._idade = valor
pessoa = Pessoa(25)
print(pessoa.idade)

pessoa.idade = 18
print(pessoa.idade)

pessoa.idade = -1

#ex 3
class Retangulo:
    def __init__(self, altura: float, largura: float):
        self._altura = altura
        self._largura = largura


    @property
    def area(self) -> float:
        return self._altura * self._largura


retangulo = Retangulo(5, 3)
print(f"Área do retângulo: {retangulo.area: .1f}")

retangulo_decimal = Retangulo(2.5, 4)
print(f"Área do retângulo decimal: {retangulo_decimal.area}")

#ex 4 exibir um cenario em que preco é um atributo publico e exibir um erro que poderia acontecer
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

notebook.preco = -1500.00 #alteração direta
print(f"Preço atualizado indevidamente: R$ {notebook.preco}") 


print(notebook.venderProduto(3))   
print(notebook.estoque)            

print(notebook.venderProduto(50))  
print(notebook.estoque)            

print(notebook.reporProduto(20))    
print(notebook.estoque)             

print(notebook.reporProduto(-5))    
print(notebook.estoque)           

#ex 5 integrador
class Termometro():
    def __init__(self, celsius,fahrenheit):
          self.celsius = celsius
          self.fahrenheit = fahrenheit

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperatura):
        if temperatura < -273.15:
            raise ValueError("Temperatura abaixo de zero absoluto não pode.")
        self._celsius = temperatura
        self._fahrenheit = (temperatura * 9 / 5) + 32

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, temperatura):
        celsius = (temperatura - 32) * 5 / 9
        if celsius < -273.15:
            raise ValueError("Temperatura abaixo de zero absoluto não pode.")
        self._fahrenheit = temperatura
        self._celsius = celsius


termometro = Termometro(25, 77)
print(f"Celsius: {termometro.celsius}")
print(f"Fahrenheit: {termometro.fahrenheit}")

termometro.celsius = 30
print(f"Após alterar Celsius, Fahrenheit: {termometro.fahrenheit}")

termometro.fahrenheit = 68
print(f"Após alterar Fahrenheit, Celsius: {termometro.celsius}")

try:
    termometro.celsius = -300
except ValueError as erro:
    print(erro)
