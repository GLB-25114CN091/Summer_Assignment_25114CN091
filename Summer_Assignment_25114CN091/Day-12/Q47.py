# Fibonacci series up to n terms
def fibonacci_series(n: int):
    if n <= 0:
        print("Invalid input. n must be positive.")
        return
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Input
try:
    n = int(input("Enter number of terms: "))
    fibonacci_series(n)
except ValueError:
    print("Invalid input. Please enter an integer.")
