peso = float(input("Peso da encomenda: "))
limite = 30
multa_kg = 3

if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_kg
    print(f"Peso: {peso}, excesso: {excesso}")
    print("Valor da multa: R$", multa)
else:
    print("Peso dentro do limite", peso)
