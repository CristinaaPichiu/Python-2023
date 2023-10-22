def count_bits(number):
    count = 0

    '''
     operația de &: pentru a verifica dacă cel mai din dreapta bit al lui number este 1 sau 0
     dacă este 1, atunci se incrementează count cu 1.
     
     operația de deplasare la dreapta >> pentru a elimina cel mai din dreapta bit din number
     impartire la 2
    '''

    while number:
        count += number & 1
        number >>= 1
    return count

# Example usage:
if __name__ == "__main__":
  number = 24
result = count_bits(number)
print(f"Numarul de biti in  {number} este {result}")