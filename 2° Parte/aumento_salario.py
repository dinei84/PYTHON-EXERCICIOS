#     AUMENTO DE SALARIOS

nome = (input('Digite o nome do funcionario: '))
salario = float(input('Digite o valor do salario atual do funcionario: '))
aumento = int(input('Digite a porcentagem do aumento do salario: '))

porc2 = aumento / 100
porc = salario * porc2
aumentoreal = porc + salario

print('O funcionario {} recebera um aumento de {}% e seu salario sera de: R${:.02f}'.format(nome, aumento, aumentoreal))