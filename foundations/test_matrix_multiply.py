from matrix_multiply import *

A = [
    [1, 1],
    [0, 1],
    [0, 1]
]

B = [
    [1, 2, 3],
    [1, 0, 1]
]

C = matrix_multiply_recursive(A, B)
print(C)

C = matrix_multiply(A, B)
print(C)
