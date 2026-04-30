numeros = []

while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    numeros.append(n)

valor = int(input("Digite o valor que deseja procurar: "))

i = 0
while i < len(numeros):
    if numeros[i] == valor:
        print("Encontrado!")
        break
    i += 1
else:
    print("Não encontrado!")