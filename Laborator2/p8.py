def filter_strings_by_ascii(x=1, strings=None, flag=True):
    # Verificăm dacă lista de șiruri a fost furnizată; altfel, creăm o listă goală
    if strings is None:
        strings = []

    filtered_lists = []

    for string in strings:
        filtered_characters = []

        for char in string:
            ascii_code = ord(char)

            if (flag and ascii_code % x == 0) or (not flag and ascii_code % x != 0):
                filtered_characters.append(char)

        filtered_lists.append(filtered_characters)

    return filtered_lists

if __name__ == "__main":
    x = 2
    strings = ["test", "hello", "lab002"]
    flag = False

    result = filter_strings_by_ascii(x, strings, flag)
    print(result)
