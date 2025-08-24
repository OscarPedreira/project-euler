import numpy as np
import time


def count_divisors(n):
    """Counts divisors for a single number 'n' efficiently."""
    # We only need to check up to the square root of n.
    limit = int(np.sqrt(n))
    # Count divisors in pairs. If 'i' is a divisor, so is 'n / i'.
    # We use a generator expression with sum() which is very fast.
    num_divisors = sum(2 for i in range(1, limit + 1) if n % i == 0)

    # If n is a perfect square, we counted its root twice, so we subtract one.
    if limit * limit == n:
        num_divisors -= 1

    return num_divisors


# --- Main Logic ---
start_time = time.time()

batch_size = 10000
start_n = 1
found = False

while not found:
    # 1. Generate a large batch of natural numbers
    natural_numbers = np.arange(start_n, start_n + batch_size)

    # 2. Generate a batch of triangle numbers using cumulative sum
    # We need the last triangle number from the previous batch to continue the sum.
    last_triangle = (start_n * (start_n - 1)) // 2
    triangle_numbers = np.cumsum(natural_numbers) + last_triangle

    # 3. Apply our fast divisor counting function to the entire batch
    # A list comprehension is often faster than np.vectorize for this.
    divisor_counts = np.array([count_divisors(num) for num in triangle_numbers])

    # 4. Check if any number in this batch satisfies the condition
    if np.any(divisor_counts > 500):
        # Find the index of the first number with > 500 divisors
        first_solution_index = np.argmax(divisor_counts > 500)

        # Get the corresponding triangle number and its divisor count
        solution_triangle = triangle_numbers[first_solution_index]
        solution_divisors = divisor_counts[first_solution_index]

        print(f"🎉 Found Solution!")
        print(f"Triangle Number: {solution_triangle}")
        print(f"Number of Divisors: {solution_divisors}")

        found = True  # Set flag to exit the while loop

    # Prepare for the next batch
    start_n += batch_size

end_time = time.time()
print(f"\nRuntime: {end_time - start_time:.4f} seconds")
