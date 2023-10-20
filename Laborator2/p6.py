"""
     6. Write a function that receives as a parameter a variable number of lists and a whole number x.
      Return a list containing the items that appear exactly x times in the incoming lists.
"""

def find_items_appearing_x_times(x, *lists):
    # Creăm o listă pentru a stoca elementele care apar exact de x ori
    result = []

    # Inițializăm o listă goală pentru a ține evidența numărului de apariții ale fiecărui element
    counts = []

    # Parcurgem fiecare listă din argumentele primite
    for sublist in lists:
        # Iterăm prin fiecare element din lista respectivă
        for item in sublist:
            # Verificăm dacă elementul se află în lista 'counts'
            if item in counts:
                # Dacă da, obținem indexul elementului
                index = counts.index(item)
                # Incrementăm numărul de apariții pentru elementul respectiv
                counts[index + 1] += 1
            else:
                # Dacă elementul nu se află în lista 'counts', îl adăugăm și inițializăm numărul de apariții cu 1
                counts.append(item)
                counts.append(1)

    # Parcurgem lista 'counts' pentru a verifica care elemente au apărut de exact x ori
    for i in range(0, len(counts), 2):
        if counts[i + 1] == x:
            result.append(counts[i])

    return result


if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]

    x = 2
    lists = [list1, list2, list3, list4]
    result = find_items_appearing_x_times(x, *lists)
    print(f"Elementele care apar de exact {x} ori sunt: {result}")






