palavra = input("Digite uma palavra: ")

inicio = 0
fim = len(palavra) - 1
eh_palindromo = True

while inicio < fim:
    if palavra[inicio] != palavra[fim]:
        eh_palindromo = False
        break
    inicio += 1
    fim -= 1

if eh_palindromo:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")