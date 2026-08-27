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


# Revisao 
class Produtos():
    def __init__(self, preco):
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido!")
        self._preco = valor

    def aplicarDesconto(self, percentual):
        return self.preco * (1 - percentual / 100)

produto = Produtos(100)
print(produto.aplicarDesconto(10))  # 90.0


# ============================================================
# NOVOS EXERCÍCIOS - ENCAPSULAMENTO
# ============================================================
# Faça os exercícios abaixo sem consultar uma solução pronta.
# Em cada classe, use atributos privados com underline, properties,
# setters para validar os valores e métodos para executar ações.
# Teste também valores inválidos usando try/except.


# EXERCÍCIO 6 - Conta bancária protegida
# Crie uma classe Conta com os atributos privados _titular e _saldo.
# Crie uma property somente para leitura chamada saldo.
# Crie depositar(valor), aceitando apenas valores maiores que zero.
# Crie sacar(valor), impedindo saque maior que o saldo.
# Retorne mensagens informando o resultado de cada operação.
# Teste depósito válido, saque válido e duas operações inválidas.

class Conta:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self._saldo:.2f}"

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo:
            raise ValueError(f"Saldo insuficiente. Saldo atual: R$ {self._saldo:.2f}")
        
        self._saldo -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self._saldo:.2f}"
if __name__ == "__main__":
    # Criando a conta
    minha_conta = Conta("João", 1000.0)
    print(f"Titular: {minha_conta._titular}")
    print(f"Saldo inicial: R$ {minha_conta.saldo:.2f}\n")

    # 1. Teste de depósito válido
    print(minha_conta.depositar(500.0))

    # 2. Teste de saque válido
    print(minha_conta.sacar(200.0))

    # 3. Testes de operações inválidas (descomente para testar as exceções)
    try:
        minha_conta.depositar(-50)
    except ValueError as e:
        print(f"Erro capturado (Depósito inválido): {e}")

    try:
        minha_conta.sacar(5000)
    except ValueError as e:
        print(f"Erro capturado (Saque maior que o saldo): {e}")


# EXERCÍCIO 7 - Aluno e nota
# Crie uma classe Aluno com nome e nota.
# A nota deve ser uma property com setter.
# Aceite somente notas entre 0 e 10.
# Crie aprovado(), retornando True se a nota for maior ou igual a 6.
# Teste uma nota válida e uma nota fora do intervalo.
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @property
    def nota(self):
        return self._nota 

    @nota.setter
    def nota(self, valor):
        if valor < 0 or valor > 10:
            raise ValueError("Apenas notas entre 0 e 10 são permitidas")
        self._nota = valor

    def aprovado(self) -> bool:
        return self.nota >= 6
aluno = Aluno("Diogo", 6)
print(aluno.aprovado())

try:
    alunoTeste = Aluno("Pedro", -1)
except ValueError as erro:
    print(f"Erro: {erro}")

# EXERCÍCIO 8 - Produto com estoque
# Crie uma classe EstoqueProduto com nome, preco e quantidade.
# Valide o preco para que nunca seja menor ou igual a zero.
# Valide a quantidade para que nunca seja negativa.
# Crie vender(quantidade), recusando vendas maiores que o estoque.
# Crie repor(quantidade), aceitando somente quantidades maiores que zero.
# Crie valor_total(), retornando preco vezes quantidade.
class EstoqueProduto():
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    @property 
    def preco(self):
        return self._preco 

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("Preço abaixo ou igual a zero não podem.")
        self._preco = valor

    @property 
    def qtd(self):
        return self._qtd

    @qtd.setter
    def qtd(self, valor):
        if valor < 0:
            raise ValueError("Quantidade negativa não pode.")
        self._qtd = valor

    def vender(self, qtd):
        if qtd > self.qtd:
            raise ValueError("Quantidade maior que estoque, venda negada.")
        self.qtd -= qtd
    def repor(self, qtd):
        if qtd > 0:
            self.qtd += qtd
    def valorTotal(self):
        return self.preco * self.qtd

produto = EstoqueProduto("Mouse", 50, 20)
print(produto.valorTotal()) #retorna 1000 

produto.vender(5)
print(produto.qtd) #15 no estoque
print(produto.valorTotal())

produto.repor(25)
print(produto.qtd) #40 no estoque após repor

try:
    produto.vender(999)         
except ValueError as erro:
    print(f"Erro: {erro}")

try:
    produto2 = EstoqueProduto("Teclado", -10, 5)  
except ValueError as erro:
    print(f"Erro: {erro}")

try:
    produto.qtd = -1            
except ValueError as erro:
    print(f"Erro: {erro}")
