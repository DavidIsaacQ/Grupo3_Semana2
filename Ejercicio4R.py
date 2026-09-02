# Ejercicio 4 - Contar y sumar pares del 1 al 20

contador = 0
suma = 0
for i in range (0, 21, 2):
    contador += 1
    suma += i
print(f"Se contaron {contador-1} numeros pares y la suma total de ellos es {suma}")