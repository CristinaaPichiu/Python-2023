def validate_dict(rules, dictionary):
    keys_found = set()  # Un set pentru a urmări cheile găsite în reguli
    result = True
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value:
                result = False
            keys_found.add(key)  # Adăugăm cheia în set-ul de chei găsite

    # Verificăm dacă toate cheile din dicționar au fost găsite în reguli
    if set(dictionary.keys()) != keys_found:
        result = False

    return result


if __name__ == "__main__":
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "this", "is", "valid")}
    data = {
        "key1": "come inside, it's too cold out",
        "key2": "start your day in the middle of winter",
        "key3": "this is not valid"

    }

result = validate_dict(rules, data)
print(result)  # Acesta va returna False pentru că "key3" nu apare în reguli
