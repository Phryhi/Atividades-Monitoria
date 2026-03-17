salario = float(input("Salario: "))

if salario < 500:
  reajuste = salario + (salario * 0.15)
  print("Reajuste: ", reajuste)
elif salario >= 500 and salario < 1000:
  reajuste = salario + (salario * 0.10)
  print("Reajuste: ", reajuste)
else:
  reajuste = salario + (salario * 0.05)
  print("Reajuste: ", reajuste)
