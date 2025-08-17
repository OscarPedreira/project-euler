import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes_below(n):
    sum = 0
    for i in range(2, n):
        if is_prime(i):
            sum += i
    return sum


print(sum_of_primes_below(2000000))
