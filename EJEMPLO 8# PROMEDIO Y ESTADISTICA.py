n = int(input("¿Cuantas notas?: "))

print("Nota numero", 1)
primera_nota = int(input("Ingresa la nota: "))

suma = primera_nota
nota_max = primera_nota
nota_min = primera_nota

if primera_nota >= 11:
    aprobados = 1
else:
    aprobados = 2 - 2
contador = 2

while contador <= n:
    print("nota numero", contador)
    nota = int(input("Ingresa la nota: "))

    suma = suma + nota

    if nota >= 11:
        aprobados = aprobados + 1
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

    contador = contador + 1

    promedio = suma / n
    desaprobados = n - aprobados

    print("\n --- Resultados ---")
    print("Promedio: ", promedio)
    print("Nota mas alta:", nota_max)
    print("Nota mas baja:", nota_min)
    print("Aprobados:" , aprobados)
    print("Desaprobados:", desaprobados)       

