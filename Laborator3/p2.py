"""
   Write a function that receives a string as a parameter and returns a dictionary in which the keys are
   the characters in the character string and the values are the number of occurrences of that character
   in the given text.
"""


def character_count(string):
    # empty dictionary to store the character counts
    char_count = {}

    for char in string:
        # check if the character is already in the dictionary
        if char in char_count:
            # if it is, increment the count
            char_count[char] += 1
        else:
            # if it's not, add it to the dictionary with a count of 1
            char_count[char] = 1

    return char_count


if __name__ == "__main__":
    text = "Ana has apples."
    result = character_count(text)
    print(result)
