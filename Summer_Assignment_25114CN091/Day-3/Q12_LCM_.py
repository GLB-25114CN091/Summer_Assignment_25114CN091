def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm_result = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")