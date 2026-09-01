# #Solicita un número y muestra su tabla de 
# multiplicar del 1 al 10 usando una estructura 
# repetitiva Para

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(1,11):
    print(f"{numero} * {i} = {i*numero}")