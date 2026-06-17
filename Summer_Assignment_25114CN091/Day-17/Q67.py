def intersection_arrays(arr1, arr2):
    return list(set(arr1) & set(arr2))

a = [1, 2, 3]
b = [2, 3, 4]
print("Intersection:", intersection_arrays(a, b))
