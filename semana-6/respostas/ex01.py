cod = int(input("código: "))

match cod:
  case 1:
    print("alimento não perecível")
  case 2 | 3 | 4:
    print("alimento perecível")
  case 5 | 6:
    print("vestuário")
  case  7:
    print("higiene pessoal")
  case 8 | 9 | 10:
    print("limpeza e utensílios domésticos")
  case _:
    print("código inválido")
