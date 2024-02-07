def multiply_numbers_from_range(start, finish):
    sum = 1
    i = start
    while i <= finish:
        sum = sum * i
        i = i + 1
    return sum