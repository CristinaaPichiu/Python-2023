#2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def is_prime(n):
    if n < 2:
        return  False
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

if __name__ == "__main__":

      print(is_prime(11)) # True
      print(is_prime(2)) # False
      numbers=[1,2,3,4,5,6,7,8,9,20,23]
      print(find_prime_numbers(numbers))



