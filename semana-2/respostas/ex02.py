tempo = float(input("Tempo(h): "))
velocidade = int(input("Velocidade(km/h): "))

distancia = velocidade * tempo
total = distancia / 12

print(f"Quantidade necessária: {total:.3f}")
