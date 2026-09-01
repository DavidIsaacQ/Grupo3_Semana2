# #Solicita dos números y un operador (+, -, *, /). Usa una estructura 
# Según para determinar la operación. Maneja el caso de división por 
# cero con una condicional

numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese un segundo numero: "))

opcion = int(input("Ingrese una opcion (1 al 4)"))
print ("Elija la operacion que desee realizar: ")
print ("(1) Suma")
print ("(2) Resta")
print ("(3) Multiplicacion")
print ("(4) Division")

if opcion == 1:
    print (f"La suma es: {numero1 + numero2}")
elif opcion == 2:
    print (f"La resta es: {numero1 - numero2}")
elif opcion == 3:
    print (f"La multiplicacion es: {numero1 * numero2}")
elif opcion == 4:
    if numero2 == 0:
        print("Error, no se puede dividir entre 0")
    else:
        print (f"La division es: {numero1 / numero2}")