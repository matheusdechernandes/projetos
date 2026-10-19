# Atividade: Controle de Níveis de Água
# Curso Técnico em Desenvolvimento de Sistemas

from colorama import Fore, Style, init

# Inicia a biblioteca Colorama
init()

# Lista com as situações do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para escolher a cor de acordo com o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Style.RESET_ALL


# Nível usado na simulação (altere de 1 a 5 para testar)
nivel_atual = 3

print("=== CONTROLE DE NÍVEIS DE ÁGUA ===")

# Confere se o nível informado existe na lista
if nivel_atual >= 1 and nivel_atual <= len(niveis):
    situacao = niveis[nivel_atual - 1]
    cor = definir_cor(nivel_atual)

    print(cor + "Nível " + str(nivel_atual) + ": " + situacao + Style.RESET_ALL)
else:
    print("Nível inválido! Informe um valor entre 1 e 5.")
