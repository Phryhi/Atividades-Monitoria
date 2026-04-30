numeros = []

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    numeros.append(n)

i = 0
print("Números maiores que 10:")
while i < len(numeros):
    if numeros[i] > 10:
        print(numeros[i])
    i += 1