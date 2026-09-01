# #Solicita dos números enteros al usuario y 
# determina cuál es el mayor. Si son iguales, 
# indica que son iguales. Usa estructuras 
# condicionales

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese un segundo numero entero: "))

if numero1 > numero2:
    print (f"el numero {numero1} es > que el numero {numero2}")
elif numero2 > numero1:
    print (f"el numero {numero2} es > que el numero {numero1}")
else:
    print (f"el numero {numero1} es igual al numero {numero2}")

