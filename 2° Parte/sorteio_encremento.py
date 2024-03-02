#   EXERCICIO DE SORTEIO MAIS SOMA DOS NUMEROS

from random import sample
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o quarto número: '))
n5 = int(input('Digite o quinto número: '))
n6 = int(input('Digite o sexto número: '))
n7 = int(input('Digite o sétimo número: '))
n8 = int(input('Digite o oitavo número: '))

lista1 = [n1, n2, n3, n4]
lista2 = [n5, n6, n7, n8]

numeros_lista1 = sample(lista1, 2)
numeros_lista2 = sample(lista2,2)

print(f"Números sorteados da primeira lista: {numeros_lista1}")
print(f"Números sorteados da segunda lista: {numeros_lista2}")


soma = sum(numeros_lista1) + sum(numeros_lista2)

print('A soma dos numeros foi {}'.format(soma))

if soma % 2 == 0:
    print('O número é par!!')
else:
    print('O número é impar!!')