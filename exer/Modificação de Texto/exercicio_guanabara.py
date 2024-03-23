#frase = 'Claudinei Almeida Souza'

# nomeupper = nome.upper()
# nomelower = nome.lower()
# nometrip = nome.strip()
# nomejunto = ''.join(nome.split())  # Remove os espaços e junte os caracteres
#dividindo = nome.split()


#print('O nome em todo maiusculo é: {}'.format(nomeupper))
#print(f'O nome todo em letras minusculas é {nomelower}')
#print(f'O nome fatiado fica {nometrip}')
# print(f'O nome sem espaços fica {nomejunto}')
# print(f'A contagem de caracteres é de {len(nomejunto)}')
#print(f'A contagem de espaços é: {nome.count(" ")}')  # Conta os espaços
#print(f'A frase dividida em index: {dividindo}')


#              CONTADOR DE LETRAS USANDO IA

# frase = "Claudinei Almeida Souza"

# Encontre a primeira palavra dividindo a frase pelo espaço em branco
# palavras = frase.split()
# primeira_palavra = palavras[0]

# Inicialize um contador de letras
# contador_letras = 0

# Itere sobre os caracteres da primeira palavra e conte apenas as letras
# for letra in primeira_palavra:
#     if letra.isalpha():
#         contador_letras += 1

# print(f"A quantidade de letras na primeira palavra é: {contador_letras}")


#               CONTADOR DE LETRAS USANDO OPERADORES SIMPLES

# frase = "Claudinei Almeida Souza"

# Divida a frase em palavras usando split() e pegue a primeira palavra
# primeira_palavra = frase.split()[0]

# Conte o número de letras na primeira palavra usando len()
# quantidade_letras = len(primeira_palavra)

# print(f"A quantidade de letras na primeira palavra é: {quantidade_letras}")

#          PRATICANDO


frase = 'Francisco Alves de Oliveira Moreira Santos'

quarta_palavra = frase.split()[4]
quantidade_letras = len(quarta_palavra)
print(f'A quantidade de letras do primeiro nome é: {quantidade_letras}')