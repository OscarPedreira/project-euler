import math


def largest_prime_factor_finder(number):
    factor_primes = []
    final_set = []
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            factor_primes.append(i)
    factor_primes.sort(reverse=True)
    for i in factor_primes:
        for t in range(2, i-1):
            if i % t == 0:
                break
        else:
            final_set.append(i)
    return final_set[0]

result = largest_prime_factor_finder(600851475143)
print(result)


