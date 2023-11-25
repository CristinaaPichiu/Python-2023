import random
import string

def generate_password(length=15, use_special=True, use_numbers=True, use_mixed_case=True):
    characters = string.ascii_letters
    if use_special:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    if use_mixed_case:
        password = ''.join(random.choice(characters) for _ in range(length))
    else:
        password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    return password

