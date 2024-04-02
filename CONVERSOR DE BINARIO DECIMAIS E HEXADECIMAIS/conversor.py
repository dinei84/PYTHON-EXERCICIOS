def bin_to_decimal(binary):
    try:
        return int(binary, 2)
    except ValueError:
        print("Erro: O número binário inserido é inválido.")
        return None

def decimal_to_bin(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hex(decimal):
    return hex(decimal)[2:]

def print_menu():
    print("Escolha o tipo de conversão:")
    print("1. Binário para Decimal")
    print("2. Decimal para Binário")
    print("3. Decimal para Octal")
    print("4. Decimal para Hexadecimal")
    print("5. Sair")

def main():
    while True:
        print_menu()
        choice = input("Digite sua escolha (1/2/3/4/5): ")

        if choice == '1':
            binary = input("Digite o número binário: ")
            decimal = bin_to_decimal(binary)
            if decimal is not None:
                print("Decimal:", decimal)
        elif choice == '2':
            decimal = int(input("Digite o número decimal: "))
            print("Binário:", decimal_to_bin(decimal))
        elif choice == '3':
            try:
                decimal = float(input("Digite o número decimal, caso necessário, use o ponto: "))
                print("Octal:", decimal_to_octal(int(decimal)))
            except ValueError:
                print("Erro: O número decimal inserido é inválido.")
        elif choice == '4':
            decimal = int(input("Digite o número decimal: "))
            print("Hexadecimal:", decimal_to_hex(decimal))
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
