def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd_result = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")