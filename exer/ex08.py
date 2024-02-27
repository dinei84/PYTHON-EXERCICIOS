#          CONVERSOR DE MEDIDAS DE CM PARA ...

n = float(input('Digite o valor a ser convertido: '))

km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('O valor de {} cm em km é: {}'.format(n, km))
print('O valor de {} cm em hm é: {}'.format(n,hm ))
print('O valor de {} cm em dam é: {}'.format(n, dam))
print('O valor de {} cm em dm é: {}'.format(n, dm))
print('O valor de {} cm em cm é: {}'.format(n, cm))
print('O valor de {} cm em mm é: {}'.format(n, mm))