#Crea una función que determine si un número es primo.
#Luego muestra todos los números primos desde 2 hasta N.

#Función que verifica si un número es primo

def es_primo(numero):

    if numero < 2:

        return False

    for divisor in range(2, int(numero ** 0.5) + 1):

        if numero % divisor == 0:

            return False

    return True

#Número límite de entrada

numero_n = int(input("Ingrese un número N: "))

#Mostrar números primos

print(f"Números primos desde 2 hasta {numero_n}:")

for numero in range(2, numero_n + 1):

    if es_primo(numero):

        print(numero)