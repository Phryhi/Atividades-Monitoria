cod = int(input("código: "))
quantidade = int(input("quantidade: "))

match cod:
  case 100:
    calculo = quantidade * 17.50
    print(f"valor final: {calculo}")
  case 101:
    calculo = quantidade * 28.10
    print(f"valor final: {calculo}")
  case 102:
    calculo = quantidade * 30.60
    print(f"valor final: {calculo}")
  case 103:
    calculo = quantidade * 23
    print(f"valor final: {calculo}")
  case 104:
    calculo = quantidade * 24.50
    print(f"valor final: {calculo}")
  case 105:
    calculo = quantidade * 5
    print(f"valor final: {calculo}")
  case _:
    print("código inválido")
