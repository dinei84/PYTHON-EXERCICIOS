n = 0
n2 = 0

print(n)
while n < 3:
    n = n + 1
    print(n)
    while n <= 377:        
        n = n + n2
        print(n)
        n2 = n2 + n
        print(n2)
        
