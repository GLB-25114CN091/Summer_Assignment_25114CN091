def find_max(a, b):
    return a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Maximum =", find_max(x, y))
