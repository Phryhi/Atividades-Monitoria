numeros = []

for i in range(10):
    n = int(input("Digite um número: "))
    numeros.append(n)

media = sum(numeros) / len(numeros)

maiores = []
for num in numeros:
    if num > media:
        maiores.append(num)

print("Média:", media)
print("Números maiores que a média:", maiores)