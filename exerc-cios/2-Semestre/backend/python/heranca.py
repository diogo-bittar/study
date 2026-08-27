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