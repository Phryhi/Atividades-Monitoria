count = 0

while True:
    produto = float(input("Valor do produto: "))
    count += produto

    add = input("Adicionar mais um produto?(s/n) ").lower()

    if add != "s":
        print("valor total:", count)
        break
