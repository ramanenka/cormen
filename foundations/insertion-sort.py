import random
import time

a = [random.random() for i in range(10000)]


def insertion_sort(a):
    if len(a) < 2:
        return

    m = 1
    while m < len(a):
        pos = 0
        while a[pos] < a[m]:
            pos += 1

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
