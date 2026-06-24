from defs import pedirNome, pedirNotas, situacaoAluno

print("\n**********************************")
print("Sistema de notas. Seja Bem-Vindo!")
print("**********************************\n")

alunos = []
while True:
    nome = pedirNome()
    notas = pedirNotas()
    alunos.append((nome, notas))
    
    continuar = input("Adicionar outro aluno? (s/n): ").lower()
    if continuar != "s":
        break

print("\n=== RESULTADO FINAL ===")
for nome, notas in alunos:
    print(situacaoAluno(nome, notas))

