n = int(input("Ingrese un numero N: "))
print("Numeros primos: ")
for num in range(2, n + 1):
    N = True

    raiz = int(num * 0.5)

    for i in range (2, raiz +1):
        if num % i == 0:
            N = False
            break
    if N:
        print(num)    