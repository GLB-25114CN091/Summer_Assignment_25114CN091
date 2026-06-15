def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
print(rotate_right(arr, 2))  
