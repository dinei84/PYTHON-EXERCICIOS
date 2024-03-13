homens_selec = 0
mulheres_selec = 0

while True:

    sexo = input('Digite o sexo [F]/[M]: ').upper()
    idade = int(input('Digite a idade: '))
    cabelo = input('Qual a cor do cabelo: [LOIRO / MORENO / CASTANHO]: ').upper()

    if (sexo == "M" and idade == 18 and cabelo == "CASTANHO") or (sexo == "F" and idade == 25 and cabelo == "LOIRO"):
        if sexo == "M":
            homens_selec += 1
        elif sexo == "F":
            mulheres_selec += 1
    
    continua = input('Deseja incluir mais alguém? [S]/ [N]: ').upper()
    if continua != "S":
        break

print('\nResultados finais:')
print('A quantidade de Homens foi: {}'.format(homens_selec))
print('A quantidade de Mulheres foi: {}'.format(mulheres_selec))
