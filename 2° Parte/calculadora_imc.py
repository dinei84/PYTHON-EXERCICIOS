#      CALCULADORA DE IMC

altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * 2)

print('O seu imc é de {0:.02f} '.format(imc))

if imc <= 18.5:
    print('Seu IMC é de {0:.02f} você está muito abaixo do peso ideal'.format(imc))
elif imc <= 24.9:
    print('Seu IMC é de {0:.02f}, você esta no peso ideal'.format(imc))
elif imc <= 29.9:
    print('Seu IMC é de {0:.02f},e você está acima do peso'.format(imc))
elif imc <= 34.9:
    print('Seu IMC é de {0:.02f} e você está com obesidade!!'.format(imc))
else:
    print('Você esta com obesidade mórbida!!!')