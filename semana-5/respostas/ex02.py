tipo = input("combustível: ")
litros = int(input("litros: "))

if tipo == "g":
  preco = litros * 2.50
  if litros > 20:
    desconto = preco * 0.05
    calc = preco - desconto
    print(calc)
  else:
    desconto = preco * 0.03
    calc = preco - desconto
    print(calc)
elif tipo == "a":
  preco = litros * 1.90
  if litros > 20:
    desconto = preco * 0.06
    calc = preco - desconto
    print(calc)
  else:
    desconto = preco * 0.05
    calc = preco - desconto
    print(calc)
else:
  print("inválido")
