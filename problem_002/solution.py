def fibonacci_sequence(limit):
    all_numbers = [1, 2]
    for i in range(limit):
        last_two = sum(all_numbers[-2:])
        all_numbers.append(last_two)
    filtered_list = [item for item in all_numbers if item < 4000000 and item % 2 == 0]
    answer  = sum(filtered_list)
    return answer

result = fibonacci_sequence(100)
print(result)