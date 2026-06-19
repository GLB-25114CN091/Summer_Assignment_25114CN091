# Matrix Transpose
def transpose_matrix(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

A = [[1, 2, 3], [4, 5, 6]]
print("Transpose:", transpose_matrix(A))
