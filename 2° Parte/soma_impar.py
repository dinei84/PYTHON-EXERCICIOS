impar = 0

for i in range(1, 8):
    if i % 2 == 1:       
        impar = impar + i
    print(i)

print(f'A soma dos numeros impares foi {impar}')