def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k] 

arr = [1, 2, 3, 4, 5]
print(rotate_left(arr, 2))  
