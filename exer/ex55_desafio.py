#     JOGO DE ADIVINHAÇÃO DE NÚMEROS

import random
from random import choice


num = random.randint(1, 5)

for i in range(1, 5):
    n = int(input('Digite o número de 1 - 5 que você acha que vai ser sorteado: '))
    if num == n:
        print('O numero sortiado foi: {}'.format(num))
        print('O numero sortiado foi igual ao seu, PARABENS!!')
    elif num < n:
        print('O numero sortiado foi: {}'.format(num))
        print('Seu nuúmero foi maior! Tente denovo!!')
    elif num > n:
        print('O numero sortiado foi: {}'.format(num))
        print('Seu nuúmero foi menor! Tente denovo!!')

    if i == 4:
        print('Acabaram suas jogadas!!')