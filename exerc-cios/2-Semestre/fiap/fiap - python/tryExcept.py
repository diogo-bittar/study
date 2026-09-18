"""
try and except in python
"""


#exercise one
while True:
    try:
        price = float(input("Price: "))
        qtd = int(input("Qtd: "))
        calcule = price * qtd
        print(f"Final price: {calcule}")
        break
    except ValueError:
        print("Entrada inválida. Apenas números são aceitos.")

#exercise two
while True:
    try:
        value = float(input("Value: "))
        people = int(input("Qtd people: "))
        total_per_person = value / people
        print(f"Total: {total_per_person:.2f}")
        break
    except ValueError:
        print("Apenas números ok?")
    except ZeroDivisionError:
        print("Por zero nao")
        
