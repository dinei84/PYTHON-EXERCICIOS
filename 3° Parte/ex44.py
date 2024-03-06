inicial = int(input('Digite o número inicial: '))
passo = int(input('Digite o passo da contagem: '))
final = int(input('digite o numero final:'))

if inicial > final:
    while final < inicial:
        print(final)
        final = final + passo
    print('Acabou!')
else:
    while inicial < final:
        print(inicial)
        inicial = inicial + passo
    print('Acabou!')