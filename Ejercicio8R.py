# Ejercicio 8 - Promedio y estadisticas

n = int(input("Ingresa la cantidad de notas: "))

suma = 0
aprobados = 0
mayor = 0
menos = 0

for i in range(1, n + 1):
    nota = float(input(f"Ingrese la nota {i}: "))

    suma = suma + nota

    if nota >=11:
        aprobados = aprobados + 1

    if i == 1:
        mayor = nota
        menor = nota
    else:
        if nota > mayor:
            mayor = nota
        if nota < menor:
            menir = nota

promedio = suma / n

print(f"El promedio es {promedio:.2f}")
print(f"La nota más alta es {mayor}")
print(f"La nota más baja es {menor}")
print(f"Aprobaron {aprobados} estudiantes")