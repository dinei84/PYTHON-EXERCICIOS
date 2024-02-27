aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a nota do primeiro semestre do aluno: '))
n2 = float(input('Digite a nota do segundo semestre do aluno: '))
n3 = float(input('Digite a nota do terceiro semestre do aluno: '))
n4 = float(input('Digite a nota do quarto semestre do aluno: '))

soma = n1 + n2 + n3 +n4
media = soma / 4

print('A média das notas do aluno {1} é {0}' .format(media, aluno))
