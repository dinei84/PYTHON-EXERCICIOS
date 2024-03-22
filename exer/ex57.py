salariof = 0
salariom = 0
somasalm = 0
somasalf = 0
sexom = 0
sexof = 0
continuar = ''
flag = True

while flag == True:
    sexo = (input('Digite o sexo do funcionário(a) [M] ou [F]: ')).upper()

    if sexo == 'M':
        salariom = float(input('Digite o salario do funcionario: '))
        sexom += 1
        somasalm = salariom + somasalm
    else:
        salariof = float(input('Digite o salario do funcionaria: '))
        sexof += 1
        somasalf = salariof + somasalf

    continuar = (input('Digite [Sair] se deseja sair ou [Enter] pra continuar: ')).upper()

    if continuar == 'SAIR':
        flag = False

print(f'Existem {sexom} funcionarios masc. e o total dos salários [Masculinos] é: {somasalm}')
print(f'Existem {sexof} funcionarias fem. e o total dos salários [Femininos] é: {somasalf}')
