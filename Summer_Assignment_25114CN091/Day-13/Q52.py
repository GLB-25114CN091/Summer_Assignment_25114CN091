n = int(input("Enter number of elements: "))
arr = [int(input(f"Element {i+1}: ")) for i in range(n)]

even_count = sum(1 for x in arr if x % 2 == 0)
odd_count = n - even_count

print(f"Even count = {even_count}, Odd count = {odd_count}")
