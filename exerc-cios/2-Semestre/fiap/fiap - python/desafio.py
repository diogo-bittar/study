desafioPY = {}
continuarChamado = True

while continuarChamado:
    print("--| Sistema de chamados |--")
    print("\n (1) Captar Problema\n",
        "(2) Consultar Problema\n",
        "(3) Média dos níveis\n",
        "(4) Mostrar todos os chamados\n",
        "(5) Sair do sistema\n")

    opc = input("Digite a sua opção: ")
    match opc:
        case "1":
            identificarChamado = input("Digite o nome do chamado: ")
            desafioPY[identificarChamado] = {
                "sistemaServico": input("Agora me informe se é: Sistema ou Serviço: "),
                "nivelProblema": int(input("Em uma escala de 1 a 3, qual o nível do problema?: ")),
                "horasAberta": float(input("Quantas horas está em aberto este chamado?: ")),
                "usuariosAfetados": int(input("E quantos usuários foram afetados?: ")),
                "ambienteProblema": input("Digite o nome do ambiente do problema: ")
            }
            print("\nBase de dados dos chamados atualizadas com sucesso! :) ")
        case "2":
            print("Procurar o chamado: ")
            buscarChamado = input("Digite o nome do chamado: ")

            if buscarChamado in desafioPY:
                print(f"O chamado '{buscarChamado}' foi encontrado!")

                dados = desafioPY[buscarChamado]

                print(f"Sistema/Serviço: {dados['sistemaServico']}\n",
                      f"Nível do problema: {dados['nivelProblema']}\n",
                      f"Horas em aberto: {dados['horasAberta']}\n",
                      f"Usuários afetados: {dados['usuariosAfetados']}\n",
                      f"Ambiente: {dados['ambienteProblema']}\n")

                if dados['nivelProblema'] >= 3 and dados['ambienteProblema'] == "producao":
                    print("Crítico")
                elif dados['nivelProblema'] >= 3 and dados['usuariosAfetados'] == 100:
                    print("Alta")
                elif dados['nivelProblema'] >= 2 or dados['horasAberta'] > 4.0:
                    print("media")
                else:
                    print("Baixa")

            else:
                print(f"\nO chamado '{buscarChamado}' não existe na base de dados.")

        case "3":
            print("Você escolheu consultar a média dos níveis")
            if len(desafioPY) == 0:
                print("Não existem chamados cadastrados.")
            else:
                quantidade_nivel_1 = 0
                quantidade_nivel_2 = 0
                quantidade_nivel_3 = 0
                soma_niveis = 0

                for _, dados in desafioPY.items():
                    nivel = dados["nivelProblema"]

                    if nivel == 1:
                        quantidade_nivel_1 += 1
                    elif nivel == 2:
                        quantidade_nivel_2 += 1
                    elif nivel == 3:
                        quantidade_nivel_3 += 1

                    soma_niveis += nivel

                total_chamados = len(desafioPY)
                media = soma_niveis / total_chamados

                print(
                    "\n===== RESUMO DOS NÍVEIS =====\n"
                    f"Total de chamados: {total_chamados}\n"
                    f"Chamados nível 1: {quantidade_nivel_1}\n"
                    f"Chamados nível 2: {quantidade_nivel_2}\n"
                    f"Chamados nível 3: {quantidade_nivel_3}\n"
                    f"Média do nível de severidade: {media:.2f}"
                )

        case "4":
            if len(desafioPY) == 0:
                print("Não existem chamados cadastrados.")
            else:
                for chamado, dados in desafioPY.items():
                    print(
                        "\n-----------------------------\n"
                        f"Chamado: {chamado}\n"
                        f"Sistema/Serviço: {dados['sistemaServico']}\n"
                        f"Nível do Problema: {dados['nivelProblema']}\n"
                        f"Horas em Aberto: {dados['horasAberta']}h\n"
                        f"Usuários Afetados: {dados['usuariosAfetados']}\n"
                        f"Ambiente: {dados['ambienteProblema']}"
                    )

        case "5":
            print("Saindo.....")
            continuarChamado = False

        case _:
            print("Opção invalida........")
