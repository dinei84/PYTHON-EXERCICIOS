# 36) Um programa de vida saudável quer dar pontos atividades físicas que podem 
# ser trocados por dinheiro. O sistema funciona assim:
#  - Cada hora de atividade física no mês vale pontos
#  - até 10h de atividade no mês: ganha 2 pontos por hora
#  - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
#  - acima de 20h de atividade no mês: ganha 10 pontos por hora
#  - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)

hrpontos = 0
pontos = 0
hpremio = 0
hr = int(input('Digite quantas horas de exercicios você fez este mês: '))


if hr < 10:
    hrpontos = hr * 2
    hrpremio = hrpontos * hr
elif hr > 10 and hr < 20:
    hrpontos = hr * 5
    hrpremio = hrpontos * hr
else:
    hr > 20
    hrpontos = hr * 10 
    hrpremio = hrpontos * hr

print('Você fez {} pontos, e o valor da sua premiação é: R${}'.format(hrpontos, hrpremio))