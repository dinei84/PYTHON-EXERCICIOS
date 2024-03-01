#   COMPARADOR DE NUMEROS

print('Vamos fazer um comparativo de números!!')
n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro números inteiro: '))

if n1 < n2:
    print('O numero {}, é menor do que o numero {}'.format(n1, n2))
elif n1 > n2:
    print('O numero {}, é maior do que o número {}'.format(n1, n2))
else: 
    print('O número {} é igual ao número {}'.format(n1, n2))