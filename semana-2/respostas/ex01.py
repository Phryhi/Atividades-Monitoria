nome = input("Nome: ")
salario = float(input("Salário: "))
vendas = float(input("Vendas: "))

calculo = vendas * 0.15
total = salario + calculo
print(f"Total: {total:.2f}")
