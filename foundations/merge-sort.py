import math
import random
import time

a = [random.random() for i in range(10000)]


def merge_sort(a, l, r, level):
    if l == r:
        return

    m = (r + l) // 2
    merge_sort(a, l, m, level + 1)
    merge_sort(a, m + 1, r, level + 1)

    lpb = l
    rpb = m + 1
    while rpb <= r and lpb <= m:
        if a[lpb] < a[rpb]:
            lpb += 1
            continue

        tmp = a[rpb]
        for i in range(rpb, lpb, -1):
            a[i] = a[i - 1]

        a[lpb] = tmp
        rpb += 1


start = time.time()
merge_sort(a, 0, len(a) - 1, 0)
print(time.time() - start)
