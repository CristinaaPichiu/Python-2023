def is_palindrome(number):
    if number < 0 or (number % 10 == 0 and number != 0):
        return False

    reversed_number = 0
    original_number = number

    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10

    return original_number == reversed_number

def count_and_find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return (palindrome_count, greatest_palindrome)

if __name__ == "__main__":
    numbers = [121, 1331, 123, 555, 1001, 45654, 78987, 42]
    palindrome_info = count_and_find_palindromes(numbers)
    print("Number of palindromes:", palindrome_info[0])
    print("Greatest palindrome:", palindrome_info[1])
