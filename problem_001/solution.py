def sum_multiples(limit):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

result = sum_multiples(1000)
print(result)
