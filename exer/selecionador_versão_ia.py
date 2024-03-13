# Variáveis para contar o número de homens e mulheres selecionados
homens_selecionados = 0
mulheres_selecionadas = 0

# Loop para continuar cadastrando pessoas até que o usuário decida parar
while True:
    # Solicitar informações do usuário
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()
    idade = int(input("Digite a idade: "))
    cor_cabelo = input("Digite a cor do cabelo (LOIRO, MORENO, CASTANHO): ").upper()

    # Verificar as condições de pré-seleção
    if (sexo == "M" and idade > 18 and cor_cabelo == "CASTANHO") or (sexo == "F" and idade > 25 and cor_cabelo == "LOIRO"):
        # Se as condições forem atendidas, incrementar o contador correspondente
        if sexo == "M":
            homens_selecionados += 1
        elif sexo == "F":
            mulheres_selecionadas += 1

    # Perguntar ao usuário se deseja continuar cadastrando pessoas
    continuar = input("Deseja cadastrar mais pessoas? (S/N): ").upper()
    if continuar != "S":
        break

# Apresentar o número de homens e mulheres selecionados
print("\nResultados:")
print(f"Total de homens selecionados: {homens_selecionados}")
print(f"Total de mulheres selecionadas: {mulheres_selecionadas}")
