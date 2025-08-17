import time

start_time = time.time()

k = 1
while True:
    is_divisible = True
    for i in range(1, 21):
        if k % i != 0:
            is_divisible = False
            break  
    if is_divisible:
        break   
    k += 1



end_time = time.time()
execution_time = end_time - start_time

print(f"Smallest divisible number: {k}")
print(f"Execution time: {execution_time} seconds")


