nome = ''
idade = 0
sexo = 0
flag = True
contm = 0
contf = 0
contotal = 0
menor_idade = float('inf')
nome_mulherjovem = ''
mulher_18 = 0
homensmaior_30 = 0
idademaior = 0



while True:
    sexo = int(input('Digite p sexo da pessoa [0] para Masculino e [1] para Feminino: '))
  
    if flag == False:
        print('')
        print('')
        break
  
    elif sexo == 0:
        nome = input('Qual o nome dele: ')
        idade = int(input('Qual a idade dele:'))
        contm += 1
        if idademaior < idade and idade > 30:
          homensmaior_30 += 1        
          idademaior = idade
  
    elif sexo == 1:
        nome = input('Digite o nome da mulher: ')
        idade = int(input('Digite a idade da mulher: '))
        contf += 1
        if idade > 18:
            mulher_18 += 1
        if idade < menor_idade:
            menor_idade = idade
            nome_mulherjovem = nome