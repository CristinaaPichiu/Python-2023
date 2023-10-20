#1. Write a function to return a list of the first n numbers in the Fibonacci string.

def generate_fibonacci(n):

    # initializare lista

    fibonacci_list = []
    if n <= 0:
        return []

    #primele 2 numere din lista
    if n >= 1:
        fibonacci_list.append(0)
    if n >= 2:
        fibonacci_list.append(1)

    #celelalte numere

    for i in range(2, n):
        next_fibonacci = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(next_fibonacci)

    return fibonacci_list

if __name__ == "__main__":

    n = 10
    result = generate_fibonacci(n)
    print(result)
