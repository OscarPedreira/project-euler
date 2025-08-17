import math
import time

start_time = time.time()

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lcm = 1
for i in range(1, 21):
    if is_prime(i):
        power = 1
        while power * i <= 21:
            power *= i
        lcm *= power
    

end_time = time.time()
execution_time = end_time - start_time

print(f"Smallest divisible number: {lcm}")
print(f"Execution time: {execution_time} seconds")

