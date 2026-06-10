n = int(input("Enter number of elements: "))
arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

total = sum(arr)
average = total / n if n > 0 else 0

print(f"Sum = {total}, Average = {average}")
