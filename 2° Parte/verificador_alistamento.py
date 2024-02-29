#   VERIFICADOR DE ALISTAMENTO


nome = str(input('Digite seu nome: '))
nasc = int(input('Ditite o ano do seu nascimento: '))
anohj = int(input('Digite o ano atual: '))

idade = anohj - nasc
falta = nasc - anohj
ajuste = abs(falta)
faltacerto = 18 - idade

if idade >= 18:
    print('Você ja tem {} anos e ja pode se alistar!!'.format(idade))
elif idade < 17:
    print('Vecê ainda tem {} anos e ainda faltam {} anos para o alistamento!!'.format(idade, faltacerto))

