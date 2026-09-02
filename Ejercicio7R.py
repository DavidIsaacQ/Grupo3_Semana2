# Ejercicio 7 - Adivina el número

import random

numero_secreto = random.randint (1, 100)
intentos = 0

print("Adivina el número secreto del 1 al 100")

while True:
    numero = int(input("Ingresa un número: "))
    intentos = intentos + 1

    if numero < numero_secreto:
        print("El número secreto es MAYOR")
    elif numero > numero_secreto:
        print("El número secreto es MENOR")
    else:
        print(f"Correcto! lo adivinaste en {intentos} intentos")
        break
    