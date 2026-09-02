#Crea una función que reciba dos números y un operador.
#Realiza la operación correspondiente.
#Valida que no se divida entre cero.

#Función que realiza las operaciones

def calcular(numero1, numero2, operador):

    if operador == "+":

        return numero1 + numero2

    elif operador == "-":

        return numero1 - numero2

    elif operador == "*":

        return numero1 * numero2

    elif operador == "/":

        if numero2 == 0:

            return "No se puede dividir entre cero"

        else:

            return numero1 / numero2

    else:

        return "Operador no válido"

#Números de entrada

numero1 = float(input("Ingrese el primer número: "))

numero2 = float(input("Ingrese el segundo número: "))

#Operador de entrada

operador = input("Ingrese el operador (+, -, *, /): ")

#Realizar operación

resultado = calcular(numero1, numero2, operador)

#Mostrar resultado

print(f"Resultado: {resultado}")