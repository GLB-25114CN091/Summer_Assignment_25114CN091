n = int(input("Enter number of elements: "))
arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

largest = max(arr)
smallest = min(arr)

print(f"Largest = {largest}, Smallest = {smallest}")
