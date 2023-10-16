def count_occurrences(first_string, second_string):
    count = 0
    index = second_string.find(first_string)

    while index != -1:
        count += 1
        index = second_string.find(first_string, index + 1)

    return count

if __name__ == "__main__":

 first_string = input("First string: ")
second_string = input("Second string: ")

occurrences = count_occurrences(first_string, second_string)

print(f"Numarul de aparitii al sirului '{first_string}' in '{second_string}' este: {occurrences}")
