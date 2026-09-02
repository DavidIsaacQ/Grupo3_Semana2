# Solicita un número y muestra su tabla de 
# multiplicar del 1 al 10 usando una estructura 
# repetitiva Para.

print("tabla de multiplicar")

numero = int(input("ingrese un numero: "))

print(f"\n--- tabla del {numero} ---")

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado} ")