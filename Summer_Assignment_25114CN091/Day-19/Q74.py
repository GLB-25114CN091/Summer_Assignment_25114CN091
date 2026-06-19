# Matrix Subtraction
def subtract_matrices(a, b):
    rows, cols = len(a), len(a[0])
    result = [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]
    return result 
    
A = [[9, 8], [7, 6]]
B = [[5, 4], [3, 2]]
print("Subtraction:", subtract_matrices(A, B))
