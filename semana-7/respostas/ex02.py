while True:
  cot_dolar = float(input("cotação do dólar: "))
  dolar = float(input("valor (em dólar): "))

  conversao = dolar * cot_dolar
  print(conversao)

  continuar = input("continuar operação?(s/n) ").lower()

  if continuar == "n":
    break
