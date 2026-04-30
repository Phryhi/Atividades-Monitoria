numeros = []

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    numeros.append(n)

print("Números pares:")
for num in numeros:
    if num % 2 == 0:
        print(num)