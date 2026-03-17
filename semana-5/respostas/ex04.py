usuario = input("Tipo de usuário (admin, funcionario): ").lower()

if usuario == "admin" or usuario == "funcionario":
  print("Acesso liberado")
else:
  print("Acesso negado")
