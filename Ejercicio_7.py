import random

numero_secreto = random.randint(1,100)
intentos = 0

print("Adivina el numero secreto entre 1 y 100")

intento = int(input("Ingresa tu número: "))
intentos = 1

while intento != numero_secreto:
    if intento < numero_secreto:
        print("El numero secreto es MAYOR.")
    else:
        print("El numero secreto es MENOR.")
    
    intento = int(input("Intenta de nuevo: "))
    intentos += 1

print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")