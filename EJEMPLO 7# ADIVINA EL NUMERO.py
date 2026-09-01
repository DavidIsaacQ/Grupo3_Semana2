import random
secreto = int(random.random() *100 ) + 1
intentos = 0
num = 0

while num!= secreto:
    num = int (input("Adivina el numero del (1-100):"))
    intentos += 1

    if num < secreto:
        print("El numero es mayor")
    elif num > secreto:
        print("El numero es menor")

print(f"Adivinaste en {intentos} intentos")