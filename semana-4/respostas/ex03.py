x = float(input("x: "))
y = float(input("y: "))
op = input("operação: ")

if op == "+":
    resultado = x + y
elif op == "-":
    resultado = x - y
elif op == "*":
    resultado = x * y
elif op == "/":
    resultado = x / y
else:
    print("invalido")

print(resultado)

if resultado % 2 == 0:
    print("par")
else:
    print("impar")

if resultado >= 0:
    print("positivo")
else:
    print("negativo")

if resultado == int(resultado):
    print("inteiro")
else:
    print("decimal")
