def my_function(*args, **kwargs):
    positional_values = set(args)
    keyword_values = set(kwargs.values())

    count = sum(1 for value in positional_values if value in keyword_values)

    return count


# Example usage:
result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)  # This will return 3
