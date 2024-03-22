
idade = 0
qtdalunos = 0
somaidade = 0
mediaidade = 0
flag = True
    
while True:
    idade = int(input('Ditgite a idade do aluno ou [999] para sair:  '))

    if idade == 999:        
        flag = False
        print(f'A media de idade do grupo é: {mediaidade}')
        print(f'A quantidade de alunos no grupo é de: {qtdalunos}')
        

    elif qtdalunos >= 1:
        qtdalunos += 1
        somaidade = idade + somaidade        
        mediaidade = somaidade / qtdalunos
    
    else:
        qtdalunos += 1
        somaidade = idade        
        
    


