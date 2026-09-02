# Escribe un programa que solicite la base y
# altura de un rectángulo y calcule su área (A =
# base × altura) y su perímetro (P =
# 2×(base+altura)). Muestra los resultados
# formateados.

print("calculando el area de un rectangulo")

base = float (input("ingrese la base: "))
altura = float (input("ingrese la altura: "))

if base <= 0 or altura <= 0:
    print("error, base o altura deben ser mayor a cero")
    
else: 
    area = base * altura 
    perimetro = 2 * (base + altura) 

print(f"el area del rectangulo es: {area} ")
print(f"el perimetro del rectagulo es: {perimetro} ")
