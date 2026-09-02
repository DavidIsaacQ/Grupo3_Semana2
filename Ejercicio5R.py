# Ejercicio 5 - Calculadora básica (4 operaciones)

n1 = float(input("Ingrese un número: "))
n2 = float(input("ingrese el segundo número: "))
operador = input("Selecciones un operador (+, -, *, /): ")

if operador == "+":
    print(f"La suma de {n1} + {n2} es {n1+n2}")

elif operador == "-":
    print(f"La resta de {n1} - {n2} es {n1-n2}")

elif operador == "*":
    print(f"La multiplicaión de {n1} x {n2} es {n1*n2}")

else:
    operador == "/"
    if n2 == 0:
        print("Error, no se puede dividir por cero")
    else:
        print(f"La división de {n1} entre {n2} es {n1/n2:.2f}")
