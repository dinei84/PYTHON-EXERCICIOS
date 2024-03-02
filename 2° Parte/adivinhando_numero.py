#     JOGO DE ADIVINHAÇÃO DE NÚMEROS

import random
from random import choice
n = int(input('Digite o número de 1 - 5 que você acha que vai ser sorteado: '))

num = random.randint(1, 5)

if num == n:
    print('O numero sortiado foi: {}'.format(num))
    print('O numero sortiado foi igual ao seu, PARABENS!!')
elif num < n:
    print('O numero sortiado foi: {}'.format(num))
    print('Seu nuúmero foi maior! Tente denovo!!')
elif num > n:
    print('O numero sortiado foi: {}'.format(num))
    print('Seu nuúmero foi menor! Tente denovo!!')
