salario = float(input("Salário: "))
parcela = float(input("parcela: "))

if parcela > (salario * 0.3):
  print("Não aprovado")
else:
  print("Aprovado")
