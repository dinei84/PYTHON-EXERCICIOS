#    VERIFICADOR DE APROVAÇÃO

aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota do primeiro semestre do aluno: '))
nota2 = float(input('Digite a nota do segundo semestre do aluno: '))
nota3 = float(input('Digite a nota do terceiro semestre do aluno: '))
nota4 = float(input('Digite a nota do quarto semestre do aluno: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
from math import floor
print('A media do aluno {} é de {}'.format(aluno, floor(media)))

if media >= 7:
    print('O aluno {} foi aprovado !!   PARABENS!!  '.format(aluno))
else:
    print('A media do aluno {} foi {} e infelizmente ele não foi aprovado.'.format(aluno))