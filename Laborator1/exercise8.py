def count_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

# Example usage:
number = 24
result = count_bits(number)
print(f"Numarul de biti in  {number} este {result}")