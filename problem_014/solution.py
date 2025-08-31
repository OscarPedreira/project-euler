def is_even(number: int) -> bool:
    return number % 2 == 0


def collatz_sequence_length(number: int) -> int:
    length = 1
    while number != 1:
        if is_even(number):
            number = number // 2
        else:
            number = 3 * number + 1
        length += 1
    return length


largest_length = 0
largest_number = 0
for i in range(1, 1000000):
    length = collatz_sequence_length(i)
    if length > largest_length:
        largest_length = length
        largest_number = i

print(largest_number)
print(largest_length)
