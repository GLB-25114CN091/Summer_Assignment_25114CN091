# Function to calculate sum of digits
n= int(input("Enter a number:"))
Sum=0
while n > 0:
        Sum += n % 10
        n = n // 10
    
print("The sum of digits is:",Sum )