def pedirNome():
    while True:
        nome = input("Informe o nome do aluno: ").capitalize()
        
        if nome.isalpha():
            return nome
        else:
            print("Nome inválido. Use apenas letras.")

def pedirNotas():
    notas = []

    for i in range(1, 6):  # nota1, nota2, nota3
        while True:
            try:
                nota = float(input(f"Informe a nota da CP{i}: "))
                
                if nota < 0 or nota > 10:
                    print("A nota deve ser entre 0 e 10.")
                    continue

                notas.append(nota)
                break
            except:
                print("Informe um número.")

    return notas


def situacaoAluno(nome, notas):
    media = sum(notas) / len(notas)

    if media >= 7:
        return f"{nome} está aprovado com média {media:.2f}."
    elif media >= 5:
        return f"{nome} está de exame com média {media:.2f}."
    else:
        return f"{nome} está reprovado com média {media:.2f}."