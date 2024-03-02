# VAMOS VER SE É APTO A FAZER O FINANCIAMENT
# 

# REGRA: NÃO PODE ULTRAPASSAR 30% SO SALARIO

nome = str(input('O nome do cliente: '))
salario = float(input('Digite o salário do cliente: '))
empr = float(input('Digite o valor do empréstimo: '))
mesesap = int(input('Digite o tempo a ser pago, em meses: '))
jurosaa = float(input('Qual será o juros a.a: '))

limite = salario * 0.3
j = (empr * jurosaa * mesesap) / 100
m = empr + j
parcelas = m / mesesap

if parcelas > limite:
    print('O cliente {0}, ultrapassou o valor de 30% do salario, ficaria com uma parcela de {1:.03f} e não está apto a fazer o financiamento'.format(nome, parcelas))
else:
    print('O cliente {0} esta apto a financiar e sua parcela ficará no valor de {1:.02f}'.format(nome, parcelas))