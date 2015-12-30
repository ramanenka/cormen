from insertion_sort import insertion_sort


def merge_sort_with_insertions_sort(a, l, r, k, level):
    if l == r:
        return

    m = (r + l) // 2
    if m - l + 1 > k:
        merge_sort_with_insertions_sort(a, l, m, k, level + 1)
    else:
        insertion_sort(a, l, m)

    if r - m > k:
        merge_sort_with_insertions_sort(a, m + 1, r, k, level + 1)
    else:
        insertion_sort(a, m + 1, r)

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
