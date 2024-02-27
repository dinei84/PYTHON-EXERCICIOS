#         DETECTOR DE MAIOR IDADE

ano = int(input('Digite o ano atual: '))
nasc = int(input('Digite o ano do seu nascimento: '))

idade = ano - nasc

print('O ano é {0} e você tem {1} anos '.format(ano, idade))
if idade >= 18:
    print('Você tem {} anos e é maior de idade e pode votar !!!'.format(idade))
else:
    print('Você tem {} anos e não é maior de idade, não pode votar'.format(idade))