def calcular_salarios():
    somasalm = 0
    somasalf = 0
    sexom = 0
    sexof = 0

    while True:
        sexo = input('Digite o sexo do funcionário(a) [M] ou [F], ou digite "sair" para encerrar: ').upper()

        if sexo == 'SAIR':
            break

        salario = float(input('Digite o salário do funcionário: '))

        if sexo == 'M':
            sexom += 1
            somasalm += salario
        elif sexo == 'F':
            sexof += 1
            somasalf += salario
        else:
            print('Opção inválida. Por favor, digite M para masculino, F para feminino ou "sair" para encerrar.')

    return sexom, somasalm, sexof, somasalf


def main():
    sexom, somasalm, sexof, somasalf = calcular_salarios()

    print(f'Existem {sexom} funcionários masc. e o total dos salários [Masculinos] é: {somasalm}')
    print(f'Existem {sexof} funcionárias fem. e o total dos salários [Femininos] é: {somasalf}')


if __name__ == "__main__":
    main()
