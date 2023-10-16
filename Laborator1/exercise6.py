def is_palindrome(number):
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_number = 0
    original_number = number

    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10

    return original_number == reversed_number

if __name__ == "__main__":
 print(is_palindrome(121))