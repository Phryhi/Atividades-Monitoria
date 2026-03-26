print("digite a operação que deseja realizar(1-5):")
print("1. decimal para hexadecimal")
print("2. hexadecimal para decimal")
print("3. decimal para octal")
print("4. octal para decimal")
print("5. Encerrar")
op = int(input())

match op:
  case 1:
    num = int(input("número decimal: "))
    print(f"hexadecimal: {hex(num)[2:].upper()}")
  case 2:
    num = input("número hexadecimal: ")
    print(f"decimal: {int(num, 16)}")
  case 3:
    num = int(input("número decimal: "))
    print(f"octal: {oct(num)}")
  case 4:
    num = input("número octal: ")
    print(f"decimal: {int(num, 8)[2:]}")
  case 5:
    print("programa encerrado")
  case _:
    print("opção inválida")
