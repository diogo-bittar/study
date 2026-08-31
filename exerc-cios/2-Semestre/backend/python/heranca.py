"""
Módulo 3 - Herança
super() - nova função para chamar método da classe mãe
"""

# exemple
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)   # reaproveita o __init__ da classe mãe
        self.raca = raca
    def fazer_som(self):
        print(f"{self.nome} diz: Au au")


# ex1 1.	Animal → Cachorro, Gato sobrescrevendo fazer_som().
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazerSom(self):
        print("Som genérico")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def fazerSom(self):
        print(f"{self.nome} diz: AuAu")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca
    def fazerSom(self):
        print(f"{self.nome} diz: Miau")

# Instanciando os objetos
cao = Cachorro("Rex", "Pastor Alemão")
gato = Gato("Felix", "Siamês")
animal_generico = Animal("Bicho")

cao.fazerSom()
# Saída: Rex diz: AuAu
gato.fazerSom()
# Saída: Felix diz: Miau
animal_generico.fazerSom()
# Saída: Som genérico


#ex 2.	Funcionario → Gerente, usando super().__init__() e adicionando bônus ao salário
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def salarioTotal(self, bonus):
        return self.salario + bonus


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonusFixo):
        super().__init__(nome, salario)
        self.bonusFixo = bonusFixo

    def salarioTotal(self):
        return super().salarioTotal(self.bonusFixo)


g1 = Gerente("Carlos", 8000.00, 2000.00)

print(f"Nome: {g1.nome}")
print(f"Salário Base: R$ {g1.salario}")
print(f"Salário Total: R$ {g1.salarioTotal()}")

# ex 3
class Veiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, modelo, portas: int):
        super().__init__(modelo)
        self.portas = portas

class Moto(Veiculo):
    def __init__(self, modelo, cilindrada: int):
        super().__init__(modelo)
        self.cilindrada = cilindrada

carrosTeste = Carro("T-cross", 4)
print(f"Modelo do automóvel: {carrosTeste.modelo}, qtd de portas: {carrosTeste.portas}")

motosTeste = Moto("MT-06", 165)
print(f"Nome da moto: {motosTeste.modelo}, cilindradas: {motosTeste.cilindrada}")


#ex integrador
from math import pi
class FormaGeometrica:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio
    def area(self):
        area = pi * self.raio ** 2
        return area
    def perimetro(self):
        perimetro = 2 * pi * self.raio
        return perimetro

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
    def area(self):
        area = self.lado ** 2
        return area
    def perimetro(self):
        perimetro = 4 * self.lado
        return perimetro

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, ladoA, ladoB, ladoC):
        super().__init__()
        self.base = base
        self.altura = altura
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def area(self):
        area = (self.base * self.altura) / 2
        return area
    def perimetro(self):
        perimetro = sum([self.ladoA, self.ladoB, self.ladoC]) 
        return perimetro
    
circulo = Circulo(5)
print(f"Círculo -> área: {circulo.area():.2f}, perímetro: {circulo.perimetro():.2f}\n")

quadrado = Quadrado(4)
print(f"Quadrado -> área: {quadrado.area()}, perímetro: {quadrado.perimetro()}\n")

triangulo = Triangulo(6, 4, 5, 5, 6)
print(f"Triângulo -> área: {triangulo.area()}, perímetro: {triangulo.perimetro()}\n")

# testando polimorfismo: mesmo método, formas diferentes
formas = [circulo, quadrado, triangulo]
for forma in formas:
    print(f"{forma.__class__.__name__}: área={forma.area():.2f}, perímetro={forma.perimetro():.2f}")