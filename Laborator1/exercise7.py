def extract_number(text):
    num_str = ""
    found_digit = False

    for char in text:
        if char.isdigit():
            num_str += char
            found_digit = True
        elif found_digit:
            break

    if num_str:
        return int(num_str)
    else:
        return None

if __name__ == "__main__":
 text1 = "An apple is 123 USD"
print(extract_number(text1))