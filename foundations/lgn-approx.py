import math


def lgn_approx(c):
    e = 1E-3
    lower = 0
    upper = 1E100

    while True:
        midle = lower + (upper - lower) / 2
        val = math.log(midle, 2)

        print('nlgn = ', val, ' (when n = ', midle, ')')

        if c < val:
            upper = midle

        if c > val:
            lower = midle

        if abs(c - val) < e:
            return midle

print(lgn_approx(1E6))
