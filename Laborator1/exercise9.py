def most_common_letter(s):

    if not s:
        return None

    most_common = s[0]
    max_count = 0

    for letter in s:
        if letter.isalpha():
            count = s.count(letter)
            if count > max_count:
                most_common = letter
                max_count = count

    return most_common

if __name__ == "__main__":
    text = "an apple is not a tomato"
    result = most_common_letter(text)
    print(f"Litera cea mai comună este: '{result}'")


