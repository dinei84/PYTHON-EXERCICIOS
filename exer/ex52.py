def main():
    # Inicialize variáveis
    total_idade = 0
    pessoas_mais_de_18 = 0
    pessoas_menos_de_5 = 0
    maior_idade = 0

    # Laço para ler a idade de 10 pessoas
    for i in range(1, 11):
        idade = int(input(f"Digite a idade da pessoa {i}: "))
        
        # Atualiza a soma total de idades
        total_idade += idade

        # Verifica se a pessoa tem mais de 18 anos
        if idade > 18:
            pessoas_mais_de_18 += 1

        # Verifica se a pessoa tem menos de 5 anos
        if idade < 5:
            pessoas_menos_de_5 += 1

        # Atualiza a maior idade
        if idade > maior_idade:
            maior_idade = idade

    # Calcula a média de idade do grupo
    media_idade = total_idade / 10

    # Exibe os resultados
    print(f"Média de idade do grupo: {media_idade}")
    print(f"Pessoas com mais de 18 anos: {pessoas_mais_de_18}")
    print(f"Pessoas com menos de 5 anos: {pessoas_menos_de_5}")
    print(f"Maior idade lida: {maior_idade}")

if __name__ == "__main__":
    main()
