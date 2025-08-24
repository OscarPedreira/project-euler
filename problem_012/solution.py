import time
import numpy as np

triangle = []
answer = []
found_answer = False

i = 0

start_time = time.time()

while True:
    triangle.append(sum(range(0, i + 2)))
    answer = []
    for k in triangle:
        for j in range(1, max(triangle) + 1):
            if k % j == 0:
                answer.append(k)
        if any(np.bincount(answer) > 500):
            print(k)
            found_answer = True
            break
    if found_answer:
        break

    i += 1

end_time = time.time()
print(f"Runtime: {end_time - start_time:.4f} seconds")
