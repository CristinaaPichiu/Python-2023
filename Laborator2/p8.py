def function(x=1, strings=[], flag=True):
    result = []

    for s in strings:
        char_list = []
        for char in s:
            '''
            Funcția ord() din Python este folosită pentru a obține valoarea numerică a codului ASCII al unui caracter. 
            '''
            ascii_code = ord(char)
            if (flag and ascii_code % x == 0) or (not flag and ascii_code % x != 0):
                char_list.append(char)
        result.append(char_list)

    return [result]  # Wrap the result in a list to ensure it's a list of lists

# Example usage:
x = 2
strings = ["test", "hello", "lab002"]
flag = False

result = function(x, strings, flag)
print(result)
