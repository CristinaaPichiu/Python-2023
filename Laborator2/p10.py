def merge_lists(*lists):
    max_length = 0

    for lst in lists:
        length = len(lst)
        if length > max_length:
            max_length = length

    result = []

    for i in range(max_length):
        tuple_items = []
        for lst in lists:
            if i < len(lst):
                tuple_items.append(lst[i])
            else:
                tuple_items.append(None)
        result.append(tuple(tuple_items))

    return result

# Exemplu de utilizare:
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
result = merge_lists(list1, list2, list3)
print(result)
