#Crea una función que solicite N notas.
#Calcula el promedio, nota más alta, nota más baja
#y cantidad de estudiantes aprobados.

#Función que calcula las estadísticas

def calcular_estadisticas(cantidad):

    suma = 0
    nota_mayor = 0
    nota_menor = 20
    aprobados = 0

    for contador in range(cantidad):

        nota = float(input(f"Ingrese la nota {contador + 1}: "))

        suma = suma + nota

        if nota > nota_mayor:

            nota_mayor = nota

        if nota < nota_menor:

            nota_menor = nota

        if nota >= 11:

            aprobados = aprobados + 1

    promedio = suma / cantidad

    return promedio, nota_mayor, nota_menor, aprobados

#Cantidad de notas

cantidad = int(input("Ingrese la cantidad de notas: "))

#Calcular estadísticas

promedio, nota_mayor, nota_menor, aprobados = calcular_estadisticas(cantidad)

#Mostrar resultados

print(f"Promedio: {promedio}")

print(f"Nota más alta: {nota_mayor}")

print(f"Nota más baja: {nota_menor}")

print(f"Cantidad de aprobados: {aprobados}")