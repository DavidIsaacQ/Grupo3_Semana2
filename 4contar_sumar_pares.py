#Crea una función que recorra los números del 1 al 20.
#Cuenta cuántos números pares hay y calcula su suma.

#Función que cuenta y suma los números pares

def contar_sumar_pares():

    contador = 0
    suma = 0

    for numero in range(1, 21):

        if numero % 2 == 0:

            contador = contador + 1
            suma = suma + numero

    return contador, suma

#Obtener cantidad y suma de números pares

cantidad_pares, suma_pares = contar_sumar_pares()

#Mostrar resultados

print(f"Cantidad de números pares: {cantidad_pares}")

print(f"Suma de números pares: {suma_pares}")