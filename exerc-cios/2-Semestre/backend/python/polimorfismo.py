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

#aplicando o polimorfismo
animais = [cao, gato]
for a in animais:
    a.fazerSom()


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
    
#aplicando o polimorfismo  / Função que recebe qualquer objeto com método calcular_area() e imprime o resultado, sem checar o tipo.



#Integrador: folha_pagamento(funcionarios) somando salários de uma lista com Funcionario, Gerente, Estagiario, cada um calculando salário de forma diferente.

class Funcionario:
    def __init__(self, salario):
        self.salario = salario

    def calcularSalario(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, salario, bonusFixo):
        super().__init__(salario)
        self.bonusFixo = bonusFixo

    def calcularSalario(self):
        return self.salario + self.bonusFixo
        
class Estagiario(Funcionario):
    def __init__(self, salario, desconto):
        super().__init__(salario)
        self.desconto = desconto

    def calcularSalario(self):
        return self.salario - self.desconto


def folha_pagamento(funcionarios):
    total = 0

    for funcionario in funcionarios:
        total += funcionario.calcularSalario()

    return total


funcionarios = [
    Funcionario(2000),
    Gerente(3000, 500),
    Estagiario(1500, 100)
]

print(f"Total da folha: R$ {folha_pagamento(funcionarios):.2f}")


