# Inicializando a variável para armazenar o somatório
soma = 0

# Definindo a flag para controlar o loop
flag = True

# Enquanto a flag for verdadeira, continue pedindo números
while flag:
    # Pedindo o número ao usuário
    numero = int(input("Digite um número (ou 1111 para sair): "))
    
    # Verificando se o número digitado é 1111
    if numero == 1111:
        flag = False  # Alterando a flag para False para sair do loop
    else:
        soma += numero  # Somando o número ao somatório

# Mostrando o somatório dos números digitados
print("O somatório dos números é:", soma)
