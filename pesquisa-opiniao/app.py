# Pesquisa de Opinião - TudoWeb
#Entadada de dados
print("=== PESQUISA DE SATISFAÇÃO TUDOWEB ===")
print()

excelente = 0
ruim = 0

for entrevistado in range(1, 51):
    print(f"Entrevistado {entrevistado}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

#Analise dos dados

    if opiniao == 1:
        excelente = excelente + 1
        print("Resposta registrada: EXCELENTE")

    elif opiniao == 2:
        print("Resposta registrada: BOM")

    elif opiniao == 3:
        ruim = ruim + 1
        print("Resposta registrada: RUIM")

    else:
        print("Opção inválida.")

    print("-" * 35)

#saida das informações
print()
print("=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
