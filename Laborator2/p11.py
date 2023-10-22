def order_tuples_by_third_character(lst):
    result = []

    # Parcurgeți lista pentru fiecare valoare a al treilea caracter (de la 'a' la 'z')
    for char in 'abcdefghijklmnopqrstuvwxyz':
        for item in lst:
            if  item[1][2] == char: #item[1][2] se referă la al treilea caracter din al doilea element al tuplului.
                result.append(item)

    return result

# Exemplu de utilizare:
tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
result = order_tuples_by_third_character(tuples_list)
print(result)
