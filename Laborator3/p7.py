def set_operations(*sets):
    result = {}
    set_list = list(sets)

    for i in range(len(set_list)):
        for j in range(i + 1, len(set_list)):
            set_a = set_list[i]
            set_b = set_list[j]

            result[f"{set_a} | {set_b}"] = set_a | set_b
            result[f"{set_a} & {set_b}"] = set_a & set_b
            result[f"{set_a} - {set_b}"] = set_a - set_b
            result[f"{set_b} - {set_a}"] = set_b - set_a

    return result

# Example usage:
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
result_dict = set_operations(set1, set2, set3)

for key, value in result_dict.items():
    print(f"{key}: {value}")
