num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operador = input("Ingresa un operador (+, -, *, /): ")

match operador:
    case "+":
        print("Resultado:", num1 + num2)

    case "-":
        print("Resultado:", num1 - num2)

    case "*":
        print("Resultado:", num1 * num2)

    case "/":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print("Resultado:", num1 / num2)

    case _:
        print("Operador no válido.")