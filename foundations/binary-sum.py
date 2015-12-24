a = [1, 0, 1, 0, 1, 1]
b = [0, 1, 0, 1, 0, 1]
c = [None for _ in range(len(a) + 1)]

carry = 0
for i in range(1, len(a) + 1):
    c[len(c) - i] = (carry + a[len(a) - i] + b[len(b) - i]) % 2
    carry = (carry + a[len(a) - i] + b[len(b) - i]) // 2

c[0] = carry

print(c)
