#    JOGO DE JOKENPO

from random import choice
minhaescolha = str(input('Digite sua escolha entre: pedra, papel, tesoura: '))

lista = ['pedra', 'papel', 'tesoura']
escolhapc = choice(lista)


if minhaescolha == escolhapc:
    print('O computador escolheu: {}'.format(escolhapc))
    print('Empate, Vamos repetir!!')
elif minhaescolha == 'pedra' and escolhapc == 'tesoura':
    print('O computador escolheu: {}'.format(escolhapc))
    print('Você ganhou! PARABÉNS!!')
elif minhaescolha == 'papel' and escolhapc == 'tesoura':
    print('O computador escolheu: {}'.format(escolhapc))
    print('Você perdeu, QUE PENA!!')
elif minhaescolha == 'tesoura' and escolhapc == 'pedra':
    print('O computador escolheu: {}'.format(escolhapc))
    print('Você perdeu, QUE PENA!!') 
elif minhaescolha == 'tesoura' and escolhapc == 'papel':
    print('O computador escolheu: {}'.format(escolhapc))
    print('Você ganhou! PARABÉNS!!')


    