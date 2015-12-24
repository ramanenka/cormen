import math
import random
import time

a = [random.random() for i in range(10000)]


def binary_search(n, a, l, r):
    while l < r:
        m = l + (r - l) // 2
        if n < a[m]:
            r = m - 1

        if n > a[m]:
            l = m + 1

        if n == a[m]:
            l = r = m

    return l + 1 if a[l] <= n else l


def insertion_sort(a):
    if len(a) < 2:
        return

    m = 1
    while m < len(a):
        pos = binary_search(a[m], a, 0, m - 1)
        val = a[m]
        i = m
        while i > pos:
            a[i] = a[i - 1]
            i -= 1

        a[pos] = val
        m += 1

start = time.time()
insertion_sort(a)
print(time.time() - start)
