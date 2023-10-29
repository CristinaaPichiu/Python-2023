"""
   Write a function that receives as a parameter a list and returns a tuple (a, b)
   representing the number of unique elements in the list, and b representing the number of duplicate
   elements in the list (use sets to achieve this objective).
"""


def count_unique_and_duplicates(list):
    unique_elements = set()
    duplicate_elements = set()

    for item in list:
        if list.count(item) == 2:
            duplicate_elements.add(item)
        else:
         if list.count(item) == 1:
            unique_elements.add(item)

    return len(unique_elements), len(duplicate_elements)


# Exemplu de utilizare:
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_count, duplicate_count = count_unique_and_duplicates(my_list)
result_tuple = (unique_count, duplicate_count)

print(result_tuple)
