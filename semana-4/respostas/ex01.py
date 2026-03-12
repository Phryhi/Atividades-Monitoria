num = int(input())

if num > 0 and num < 1000:
  cent = num // 100
  dez = (num % 100) // 10
  uni = num % 10

  print(f"{num} = {cent} centenas, {dez} dezenas, {uni} unidades")
else:
  print("Inválido")
