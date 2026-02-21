import math

area = float(input("Área: "))
cobertura = area / 3
latas = math.ceil(cobertura / 16)
preco = latas * 70

print(f"Latas: {latas}, preço: {preco:.2f}")
