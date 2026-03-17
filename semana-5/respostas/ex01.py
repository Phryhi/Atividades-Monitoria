salario = float(input("Informe seu salário: "))
despesas = float(input("Despesas: "))
calc = salario- despesas

if calc >= 0:
  print("gastos dentro do orçamento")
else:
  print("Orçamento estourado") 
