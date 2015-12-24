a = [1, 4, 3, 2, 5]


def selection_sort(a): 
    for i in range(0, len(a) - 1):              # c1(n-1)
        minIndex = i                            # c2(n-1)
        for j in range(i + 1, len(a)):          # c3((n-1) + (n-2) + ... + (n-(n-1)) = n^2/2 - n/2)
            if a[j] < a[minIndex]:              # c4((n-1) + (n-2) + ... + (n-(n-1)) = n^2/2 - n/2)
                minIndex = j                    # c5*ti (best: ti = 0, worst ti = n^2/2 - n/2)

        a[i], a[minIndex] = a[minIndex], a[i]   # c6(n-1)

selection_sort(a)
print(a)


# (n-1)(n-1+n-(n-1))/2 = (n-1)n/2 = n^2/2 - n/2

# (c1 + c2 + c6)(n-1) + (c3 + c4 + c5)(n^2/2 - n/2) =>
# (c1 + c2 + c6)n - c1 - c2 - c6 + (c3 + c4 + c5)n^2/2 - (c3 + c4 + c5)/2 n => 
# ... = Theta(n^2) for worst and best cases
