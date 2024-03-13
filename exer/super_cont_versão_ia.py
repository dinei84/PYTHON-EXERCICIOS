def main():
  contmais = 0
  contmenos = 10

  while True:
    # Exibe o menu de opções
    print('\nEscolha uma opção:')
    print('1. Contagem crescente')
    print('2. Contagem regressiva')
    print('3. Limpar tela')
    print('0. Sair')

    # Lê a opção escolhida pelo usuário
    opcao = int(input('Opção: '))

    if opcao == 1:
      # Contagem crescente
      while contmais < 10:
        contmais += 1
        print(contmais)
    elif opcao == 2:
      # Contagem regressiva
      while contmenos >= 0:
        contmenos -= 1
        print(contmenos)
    elif opcao == 3:
      # Limpa a tela
      import os
      os.system('clear')
    elif opcao == 0:
      # Sai do programa
      break
    else:
      # Opção inválida
      print('Opção inválida!')

if __name__ == '__main__':
  main()
