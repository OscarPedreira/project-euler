def palindrome_finder(number):
    
    numbers_a = list(range(1, number))
    numbers_b = list(range(1, number))
    results = []

    for i in numbers_a:
        for j in numbers_b:
            product = i * j
            results.append(product)
    results.sort(reverse=True)

    for k in results:
        number_str = str(k)
        number_str_a = int(number_str[0:3])
        number_str_b_reversed = int(number_str[3:6][::-1])
        if number_str_a - number_str_b_reversed == 0:
            break
        
    return k

result = palindrome_finder(999)
print(result)



