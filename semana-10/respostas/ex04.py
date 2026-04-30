lista = [2, 5, 7, 8, 10]

contador = 0
for num in lista:
    if num % 2 != 0:
        contador += 1

print(f"{contador} números ímpares")