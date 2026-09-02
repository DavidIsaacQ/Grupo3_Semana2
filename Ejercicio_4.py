contador_pares = 0
suma_pares = 0

for i in range(1, 21):
    if i % 2 == 0:
        contador_pares += 1
        suma_pares += i

print(f"Cantidad de numeros pares encontrados: {contador_pares}")
print(f"Suma total de los numeros pares: {suma_pares}")