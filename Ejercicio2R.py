# Ejercicio 2 - Mayor de dos números

n1 = int(input("Ingrese el primer número entero: "))
n2 = int(input("Ingrese el segundo número entero: "))

if n1 > n2:
    print(f"El primer número ingresado ({n1}) es mayor al segundo número ({n2})")

elif n2 >n1:
    print(f"El segundo número ingresado ({n2}) es mayor al primer número ({n1})")
else:
    print("Los números son iguales")
    