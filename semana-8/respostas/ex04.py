n = input("Digite um número: ")

soma = 0
for digito in n:
    if int(digito) % 2 != 0:
        soma += int(digito)

print("Soma dos dígitos ímpares:", soma)