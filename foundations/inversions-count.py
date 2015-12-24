a = [1, 2, 3, 4, 5, 0, 1]


def inversions_count(a, l, r, level):
    result = 0
    if l == r:
        return result

    m = (l + r) // 2
    result += inversions_count(a, l, m, level + 1)
    result += inversions_count(a, m + 1, r, level + 1)

    lb = l
    rb = m + 1
    mn = m
    while lb <= m and rb <= r:
        if a[lb] <= a[rb]:
            lb += 1
            continue

        result += mn - lb + 1
        tmp = a[rb]
        for i in range(rb, lb, -1):
            a[i] = a[i - 1]

        a[lb] = tmp
        rb += 1
        lb += 1
        mn += 1

    return result

print(inversions_count(a, 0, len(a) - 1, 0))
print(a)
