n= int(input("Enter a number:"))
product=1
while n > 0:
        product *= n % 10
        n = n // 10
    
print("The product of digits is:",product )