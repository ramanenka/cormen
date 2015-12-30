def insertion_sort(a, l, r):
    if r + 1 - l < 2:
        return

    m = l + 1
    while m < r + 1:
        pos = l
        while a[pos] < a[m]:
            pos += 1

        val = a[m]
        i = m
        while i > pos:
            a[i] = a[i - 1]
            i -= 1

        a[pos] = val
        m += 1
