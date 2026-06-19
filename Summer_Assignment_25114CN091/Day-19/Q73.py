# Matrix Addition
def add_matrices(a, b):
    rows, cols = len(a), len(a[0])
    result = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Addition:", add_matrices(A, B))
