tipo = input("Tipo de cliente(vip, comum): ").lower()
compra = float(input("Valor compra: "))

if tipo == "vip" or compra > 100:
  desconto = compra - (compra * 0.10)
  print("Desconto aplicado")
  print("Preço atual: ", desconto)
else:
  print("Não há desconto")
