def transform_string(string):
    new_string = ""
    for i in range(0, len(string)):
        if 'A' <= string[i] <= 'Z' and i > 0:
            new_string = new_string + '_' + string[i].lower()
        else:
            new_string = new_string + string[i].lower()

    return new_string


if __name__ == "__main__":
 print(transform_string("UpperCamelCase"))
