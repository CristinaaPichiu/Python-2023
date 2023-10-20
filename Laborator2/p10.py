def merge_lists(*input_lists):
    max_length = max(len(lst) for lst in input_lists)
    result = []

    for i in range(max_length):
        tuple_items = []
        for lst in input_lists:
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
