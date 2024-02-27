#       CLACULADORA DE DESCONTOS

preco = float(input('Digite o valor do produto: '))
deconto = float(input('Digite a porcentagem (%) do desconto: '))

res = preco - (preco * (deconto / 100))
print(f'O preço final é: {res:.02f}')
