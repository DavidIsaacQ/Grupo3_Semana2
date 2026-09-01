
contador = 0
suma = 0
for i in range (1, 21):
    if i % 2 == 0:
      contador += 1
      suma += i
print(f"Se contaron , {contador}")
print(f"La suma es , {suma}")      