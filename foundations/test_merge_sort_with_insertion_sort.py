from merge_sort import merge_sort
from insertion_sort import insertion_sort
from merge_sort_with_insertions_sort import merge_sort_with_insertions_sort
import random
import time

a = [random.random() for i in range(100000)]

a1 = a[:]
start = time.time()
merge_sort(a1, 0, len(a1) - 1, 0)
print(time.time() - start)

# a2 = a[:]
# start = time.time()
# insertion_sort(a2, 0, len(a2) - 1)
# print(time.time() - start)


a3 = a[:]
start = time.time()
merge_sort_with_insertions_sort(a3, 0, len(a3) - 1, 6, 0)
print(time.time() - start)
