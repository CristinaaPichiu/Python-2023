"""
    Compare two dictionaries without using the operator "==" returning True or False.
    (Attention, dictionaries must be recursively covered because they can contain other containers
    such as dictionaries, lists, sets, etc.)

"""


def compare_dicts(dictionary1, dictionary2):
    # check if the keys from the 1st dict are equals with the keys from the 2nd

    if set(dictionary1.keys()) != set(dictionary2.keys()):
        return False

    for key in dictionary1:
        value1, value2 = dictionary1[key], dictionary2[key]

        # Dacă valorile sunt dicționare, comparăm recursiv
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        # Dacă valorile sunt liste, le comparăm recursiv
        elif isinstance(value1, list) and isinstance(value2, list):
            if not compare_lists(value1, value2):
                return False
        # Dacă valorile sunt seturi, le comparăm ca seturi
        elif isinstance(value1, set) and isinstance(value2, set):
            if value1 != value2:
                return False
        # Altfel, comparăm valorile direct
        elif value1 != value2:
            return False

    return True


def compare_lists(list1, list2):
    # Comparăm liste element cu element
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        # Dacă elementele sunt dicționare, le comparăm recursiv
        if isinstance(item1, dict) and isinstance(item2, dict):
            if not compare_dicts(item1, item2):
                return False
        # Dacă elementele sunt liste, le comparăm recursiv
        elif isinstance(item1, list) and isinstance(item2, list):
            if not compare_lists(item1, item2):
                return False
        # Dacă elementele sunt seturi, le comparăm ca seturi
        elif isinstance(item1, set) and isinstance(item2, set):
            if item1 != item2:
                return False
        # Altfel, comparăm elementele direct
        elif item1 != item2:
            return False
    return True


if __name__ == "__main__":
    dict1 = {'a': 1, 'b': [2, 3, {'x': 4}], 'c': set([5, 6])}
    dict2 = {'a': 1, 'b': [2, 3, {'x': 4}], 'c': set([5, 6])}
    result = compare_dicts(dict1, dict2)
    print(result)  # Va afișa True
