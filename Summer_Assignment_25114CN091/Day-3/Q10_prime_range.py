def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print() 
    
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
print_primes_in_range(lower, upper)