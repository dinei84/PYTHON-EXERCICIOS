def main():

    homen = 0
    mulher = 0
    idadeh = 0
    idadem = 0
    sexo = 0
    media = 0
    media_id_homens = 0
    mulhermaior = 0

    for i in range (1, 6):
        sexo = int(input('Digite [1] p/ Mascculino e [2] p/ Feminino para a {}° pessoa: '.format(i)))
        if sexo == 1:
            idadeh = int(input('Digite a idade dele: '))
            homen += 1
        elif sexo == 2:
            idadem = int(input('Digite a idade dela: '))
            mulher += 1
            if idadem > 20:
                 mulhermaior += 1            
    

    media = (idadeh + idadem) / 5
    media_id_homens = idadeh / homen

    print('Resultados:')
    print(f'A media de idade do grupo é: {media} anos')
    print(f'A media de idade dos homens é {media_id_homens:,.2f} anos')
    print(f'A quantidade de mulheres maiores de 20 anos é de: {mulhermaior}')

if __name__=='__main__':
    main()