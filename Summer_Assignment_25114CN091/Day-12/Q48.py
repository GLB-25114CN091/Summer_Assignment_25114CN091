def is_perfect(num: int) :
    if num <= 0:
        return False
    return sum(i for i in range(1, num // 2 + 1) if num % i == 0) == num

# Input (assumes valid integer input)
num = int(input("Enter a number: "))
if is_perfect(num):
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is NOT a Perfect number.")
