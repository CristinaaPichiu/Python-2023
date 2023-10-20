def order_tuples_by_third_character(lst):
    result = []

    # Parcurgeți lista pentru fiecare valoare a al treilea caracter (de la 'a' la 'z')
    for char in 'abcdefghijklmnopqrstuvwxyz':
        for item in lst:
            if len(item[1]) >= 3 and item[1][2] == char:
                result.append(item)

    return result

# Exemplu de utilizare:
tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
result = order_tuples_by_third_character(tuples_list)
print(result)
