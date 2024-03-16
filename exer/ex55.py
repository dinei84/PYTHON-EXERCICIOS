def main():

    peso = 0 
    altura = 0
    media_altura = 0
    maior_90 = 0
    menores = 0
    maiores = 0
    altura_total = 0

    for i in range(1, 4):
        peso = float(input(f"Digite o peso da {i}ª pessoa: "))
        altura = float(input(f"Digite a altura da {i}ª pessoa: "))

        altura_total += altura
    
        if peso > 90:
            maior_90 += 1
    
        if peso < 50 and altura < 1.60:
         menores += 1
    
        if altura > 1.90 and peso  > 100:
            maiores += 1

    media_altura = altura_total / 3

    print('Resultados')
    print(f'A media de altura do grupo é de {media_altura:,.2f}')
    print(f'A quantidade de pessoas que pesam menos de 50Kg e tem menos de 1.60m é: {menores}')
    print(f'A quantidade de pessoas maiores de 1.90m e tem mais de 100Kg é {maiores}')

if __name__=='__main__':
    main()