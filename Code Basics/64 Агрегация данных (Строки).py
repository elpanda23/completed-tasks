def join_numbers_from_range(first, last):
    x = str(first)
    sum = ""
    for i in range(first, last):
        x = x + str(i+1)
    return x