def move_zeroes_end(arr):
    non_zero = [x for x in arr if x != 0]
    return non_zero + [0] * (len(arr) - len(non_zero))

arr = [0, 1, 0, 3, 12]
print(move_zeroes_end(arr)) 
