#Crea un programa que genere un número aleatorio entre 1 y 100.
#El usuario debe adivinar el número.
#Indica si el número secreto es mayor o menor.

import random

#Función para adivinar el número

def adivinar_numero():

    numero_secreto = random.randint(1, 100)

    intentos = 0

    while True:

        numero = int(input("Ingrese un número entre 1 y 100: "))

        intentos = intentos + 1

        if numero < numero_secreto:

            print("El número secreto es mayor")

        elif numero > numero_secreto:

            print("El número secreto es menor")

        else:

            print("¡Adivinaste el número!")

            return intentos

#Ejecutar el juego

cantidad_intentos = adivinar_numero()

#Mostrar cantidad de intentos

print(f"Cantidad de intentos: {cantidad_intentos}")