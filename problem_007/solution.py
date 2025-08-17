import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_finder(k):
    list_primes = []
    i = 1
    while len(list_primes) < k:
        if is_prime(i):
            list_primes.append(i)
        i += 1
    list_primes.sort(reverse=True)
    return list_primes[0]


result = prime_finder(10001)
print(result)


