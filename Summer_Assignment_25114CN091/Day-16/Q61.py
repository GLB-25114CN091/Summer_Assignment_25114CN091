def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [1, 2, 4, 5, 6]  
print("Missing number:", find_missing_number(arr))
