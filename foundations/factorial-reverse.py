
def factorial_reverse(n):
    f = 2
    while n > 1:
        n /= f
        print('n/', f, ' = ', n)
        f += 1

    return f


factorial_reverse(3.15E15)
