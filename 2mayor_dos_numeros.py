# Solicita dos números enteros al usuario y 
# determina cuál es el mayor. Si son iguales, 
# indica que son iguales. Usa estructuras 
# condicionales.

print("=== MAYOR DE DOS NÚMEROS ===")

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

if num1 > num2:
    print(f"\nEl mayor es: {num1}")
elif num2 > num1:
    print(f"\nEl mayor es: {num2}")
else:
    # Si no se cumple ninguna de las anteriores, son iguales
    print(f"\nLos dos números son iguales: {num1}")

print("============================")