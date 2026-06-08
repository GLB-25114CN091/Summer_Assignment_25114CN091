def is_armstrong(num: int) :
    if num < 0:
        return False
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num
num = int(input("Enter a number: "))  # Will crash if input is not an integer
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")
