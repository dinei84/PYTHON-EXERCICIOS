#   VAMOS CALCULAR O ALUGUEL DE VEICULOS POPULARES E DE LUXO
#
#  REGRA: POPULAR R$90,00 / DIA
#  ATE 100KM R$0,20 / KM
#  ACIMA DE 100KM R$ 0,10 / KM
#  REGRA: LUXO R$150,00 / DIA
#  ATE 200KM R$0,30 / KM
#  ACIMA DE 200KM R$ 0,25 / KM

cliente = str(input('Digite o nome do cliente: '))
tipoveiculo = str(input('Digite o tipo do veiculo (Luxo) ou (Popular): '))
kmrodado = int(input('Digite quantos km o veiculo andou: '))
dia = int(input('Quantos dias o cliente ficou como carro: '))


if tipoveiculo == 'Popular':
    if kmrodado > 100:
        kmtotal = (dia * 90) + ((kmrodado - 100) * 0.1)
        print('O cliente rodou um total de {}km'.format(kmrodado))
        print('O Cliente {}, excedeu a quantidade mínima de km'.format(cliente))
        print('O total a pagar é: {}'.format(kmtotal))
    else:
        kmtotal = dia * 90
        print('O cliente rodou um total de {}'.format(kmrodado))
        print('O Cliente {}, alugou o carro por {} dias'.format(cliente, dia))
        print('O total a pagar é: {}'.format(kmtotal))

if tipoveiculo == 'Luxo':
    if kmrodado > 200:
        kmtotal = (dia * 150) + ((kmrodado - 200) * 0.25)
        print('O cliente rodou um total de {}km'.format(kmrodado))
        print('O Cliente {}, excedeu a quantidade mínima de km'.format(cliente))
        print('O total a pagar é: {}'.format(kmtotal))
    else:
        kmtotal = dia * 150
        print('O cliente rodou um total de {}'.format(kmrodado))
        print('O Cliente {}, alugou o carro por {} dias'.format(cliente, dia))
        print('O total a pagar é: {}'.format(kmtotal))
