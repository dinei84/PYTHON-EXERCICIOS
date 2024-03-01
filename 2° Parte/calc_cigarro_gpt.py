def calcular_tempo_perdido(cigarros_por_dia, anos_fumados):
    total_cigarros = cigarros_por_dia * 365 * anos_fumados
    tempo_perdido_minutos = total_cigarros * 10
    tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)  # Convertendo minutos para dias
    return tempo_perdido_dias

def main():
    cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
    anos_fumados = int(input('Quantos anos ele já fumou: '))

    dias_perdidos = calcular_tempo_perdido(cigarros_por_dia, anos_fumados)

    print(f"O fumante perderá aproximadamente {dias_perdidos:.2f} dias de vida.")

if __name__ == "__main__":
    main()
