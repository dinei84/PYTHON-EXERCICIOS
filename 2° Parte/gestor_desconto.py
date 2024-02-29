#    GESTOR DE DESCONTOS

nome = str(input('Digite o nome do cliente: '))
preco = float(input('Digite o valor do produto: '))
escolhasex = input('Digite o sexo do comprador ((m) para Masculino e (f) para Feminino): ')

if escolhasex == 'm':
    desconto = preco - (0.05 * 100)
elif escolhasex == 'f':
    desconto = preco - (0.5 * 100)

print('A compra do cliente: {}, ficou no valor de {} com desconto'.format(nome, desconto))
