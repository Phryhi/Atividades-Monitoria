x = int(input("mês(1-12): "))

match x:
  case 1 | 2 | 3:
    print("trimestre 1, verão")
  case 4 | 5 | 6:
    print("trimestre 2, outono")
  case 7 | 8 | 9:
    print("trimestre 3, inverno")
  case 10 | 11 | 12:
    print("trimestre 4, primavera")
  case _:
    print("mês inválido")
