carrosnovos = 0
carrosusados = 0
modelo = ''

while True:

    modelo = (input('Digite o modelo: [SEDAN] / [HAT] / [SUV]: ')).upper()
    ano = int(input('Qual o ano do veiculo: '))
    cor = (input('Qual a cor do Veiculo: [BRANCO] / [PRETO] / [CINZA] / [VERMELHO]: ')).upper()

    if (ano <= 2018 and modelo == "SEDAN" and cor == "VERMELHO") or (ano > 2019 and modelo == "SUV" and cor == "PRETO"):
        if ano <= 2018:
            carrosusados += 1
        elif ano > 2019:
            carrosnovos += 1
        elif modelo == "SUV":
            modelo += 1

    continua = (input('Quer continuar: [S] ou [N]: ')).upper()
    if continua != "S":
        break

print('\nResultados finais: ')
print('Carros novos (SUV) E (PRETO): {}'.format(carrosnovos))
print('Carros Usados (SEDAN) (VERMELHO): {}'.format(carrosusados))
print('Modelos SUV: {}'.format(modelo))
