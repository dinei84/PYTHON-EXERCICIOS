#   VAMOS CALCULAR A METRAGEM DO TERRENO E CLASSIFICALO
#  MEDIDA:
#  - Abaixo de 100m² = TERRENO POPULAR
#   - Entre 100m² e 500m² = TERRENO MASTER
#   - Acima de 500m² = TERRENO VIP

print('Vamos calcular a área do terreno!')

largura = int(input('Digite a çargura do terreno: '))
compri = int(input('Digite o comprimento do terreno: '))

area = largura * compri

if area < 100:
    print('O terreno tem {}m2 e é um TERRENO POPULAR'.format(area))
elif area > 100 and area < 500:
    print('O terreno tem {}m2 e é um TERRENO MASTER'.format(area))
else:
    print('O terreno tem {}m2 e é um TERRENO VIP'.format(area))