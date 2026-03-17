senha = input("Senha: ")

if len(senha) > 8 and senha != "123456":
  print("Senha válida!")
else:
  print("Senha inválida!")
