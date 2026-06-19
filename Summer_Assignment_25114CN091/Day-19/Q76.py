# Diagonal Sum
def diagonal_sum(a):
    n = len(a)
    return sum(a[i][i] + a[i][n - i - 1] for i in range(n)) - (a[n//2][n//2] if n % 2 else 0)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print("Diagonal Sum:", diagonal_sum(A))
