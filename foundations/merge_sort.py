def merge_sort(a, l, r, level):
    if l == r:
        return

    m = (r + l) // 2
    merge_sort(a, l, m, level + 1)
    merge_sort(a, m + 1, r, level + 1)

    a1 = a[l: m + 1]
    a2 = a[m + 1: r + 1]
    lb = 0
    rb = 0
    len_a1 = m + 1 - l
    len_a2 = r - m

    for i in range(l, r + 1):
        if lb < len_a1 and rb < len_a2:
            if a1[lb] < a2[rb]:
                a[i] = a1[lb]
                lb += 1
            else:
                a[i] = a2[rb]
                rb += 1

            continue

        if lb < len_a1:
            a[i] = a1[lb]
            lb += 1

        if rb < len_a2:
            a[i] = a2[rb]
            rb += 1
