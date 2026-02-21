altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

print("IMC: ", round(imc, 2))
