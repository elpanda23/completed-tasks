def square_digits(num):
    x = list(map(int, str(num)))
    for i in range(len(x)):
        x[i] = x[i] * x[i]

    x = int(''.join(map(str, x)))
    return x