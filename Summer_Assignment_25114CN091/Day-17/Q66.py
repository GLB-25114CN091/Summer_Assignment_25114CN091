def union_arrays(arr1, arr2):
    return list(set(arr1) | set(arr2))

a = [1, 2, 3]
b = [3, 4, 5]
print("Union:", union_arrays(a, b))
