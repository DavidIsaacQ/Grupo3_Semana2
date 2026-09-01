# #Escribe un programa que solicite la base y 
# altura de un rectángulo y calcule su área (A = 
# base × altura) y su perímetro (P = 
# 2×(base+altura)). Muestra los resultados 
# formateados.

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = base * altura
perimetro = 2*(base + altura)

print (f"Area: {area}  /  Perimetro: {perimetro}")
