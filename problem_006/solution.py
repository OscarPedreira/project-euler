def sum_square_difference(n):
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += i**2

    square_sum = 0
    for i in range(1, n+1):
        square_sum += i
    square_sum = square_sum**2

    return square_sum - sum_squares


result = sum_square_difference(100)
print(result)