pop_a = 80000
pop_b = 200000
anos = 0

while pop_a < pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    anos += 1

print("Anos necessários:", anos)