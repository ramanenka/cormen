import math


def nlgn_approx(c):
    k = 1
    e = 1E-6
    lower = 0
    upper = 1E14

    while True:
        midle = lower + (upper - lower) / 2
        val = midle * math.log(midle, 2)

        print(k, '\t', lower, '\t', upper)
        k += 1

        if c < val:
            upper = midle

        if c > val:
            lower = midle

        if abs(c - val) < e:
            return midle

print(nlgn_approx(3.15E15))
