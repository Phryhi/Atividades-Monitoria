numeros = []

for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

soma = 0
for num in numeros:
    soma += num

print("Soma:", soma)