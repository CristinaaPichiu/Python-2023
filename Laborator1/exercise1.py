import math

# functie definita pentru a gasi CMMDC ul unui sir de numere
# `numbers` reprezinta lista de numere
def gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

# se citesc numerele de la tastatura
# valorile introduse de user sunt salvate ca tip string

if __name__ == "__main__":


 i_numbers = input("Numerele sunt: ")

numbers = i_numbers.split()

list = []

for number in numbers:
    if number.isnumeric():
        list.append(int(number))

if len(list) < 2:
    print("Trebuie minim 2 numere")
else:
    gcd = gcd(list)
    print(f"CMMDC ul numerelor:  {list} este {gcd}")

