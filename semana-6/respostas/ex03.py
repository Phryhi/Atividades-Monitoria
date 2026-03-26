indicador = input("Deseja calcular qual indicador(n, m)? ").lower()
habitantes = int(input("Número de habitantes: "))

match indicador:
  case "n":
    nascidos = int(input("número de crianças nascidas: "))
    calc = (nascidos * 1000) / habitantes
    print("índice de natalidade: ", round(calc, 2))
  case "m":
    obitos = int(input("número de óbitos: "))
    calc = (obitos * 1000) / habitantes
    print("índice de mortalidade: ", round(calc, 2))
  case _:
    print("índice inválido")
