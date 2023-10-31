N = int(input("Введите число N: "))
    
for i in range(1, N + 1):
    for j in range(N, N - i, -1):
        print(j, end="")
        
    for _ in range(2 * (N - i)):
        print(".", end="")

    for j in range(N - i + 1, N + 1):
        print(j, end="")
    print()  

